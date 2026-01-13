import cv2
import mediapipe as mp
import asyncio
import websockets
import json
import math

# --- CONFIG ---
SENSITIVITY = 0.7  # High sensitivity for instant response
PORT = 8765

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1, 
    min_detection_confidence=0.8, 
    min_tracking_confidence=0.8
)
cap = cv2.VideoCapture(0)
clients = set()

# State for smoothing
curr_x, curr_y, curr_p = 0.5, 0.5, 0.1
curr_rx, curr_ry, curr_rz = 0, 0, 0

async def ws_handler(ws):
    clients.add(ws)
    try: await ws.wait_closed()
    finally: clients.remove(ws)

async def tracker():
    global curr_x, curr_y, curr_p, curr_rx, curr_ry, curr_rz
    
    while True:
        ret, frame = cap.read()
        if not ret: continue
        
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        res = hands.process(rgb)

        if res.multi_hand_landmarks:
            lm = res.multi_hand_landmarks[0].landmark
            
            # 1. POSITION (Middle Finger MCP)
            tx, ty = lm[9].x, lm[9].y
            
            # 2. PINCH (Size)
            dist = math.hypot(lm[8].x - lm[4].x, lm[8].y - lm[4].y)

            # 3. 3D ROTATION LOGIC
            # Yaw (Y-axis): Difference in Z between Index base (5) and Pinky base (17)
            # If index is closer than pinky, hand is turned left.
            target_ry = (lm[5].z - lm[17].z) * 15 
            
            # Pitch (X-axis): Difference in Z between Wrist (0) and Middle base (9)
            # If middle knuckles are closer than wrist, hand is tilted up.
            target_rx = (lm[0].z - lm[9].z) * 15

            # Roll (Z-axis): Angle between wrist and middle finger
            target_rz = math.atan2(lm[9].y - lm[0].y, lm[9].x - lm[0].x) + (math.pi/2)

            # --- SMOOTHING ---
            curr_x += (tx - curr_x) * SENSITIVITY
            curr_y += (ty - curr_y) * SENSITIVITY
            curr_p += (dist - curr_p) * SENSITIVITY
            curr_rx += (target_rx - curr_rx) * SENSITIVITY
            curr_ry += (target_ry - curr_ry) * SENSITIVITY
            curr_rz += (target_rz - curr_rz) * SENSITIVITY

            data = {
                "x": round(curr_x, 3),
                "y": round(curr_y, 3),
                "pinch": round(curr_p, 4),
                "rx": round(curr_rx, 3),
                "ry": round(curr_ry, 3),
                "rz": round(curr_rz, 3)
            }

            if clients:
                msg = json.dumps(data)
                await asyncio.gather(*[c.send(msg) for c in clients])

        await asyncio.sleep(0.01)

async def main():
    print(f"Server started on ws://localhost:{PORT}")
    async with websockets.serve(ws_handler, "localhost", PORT):
        await tracker()

if __name__ == "__main__":
    asyncio.run(main())