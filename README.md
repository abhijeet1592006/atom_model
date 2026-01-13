#  Real-time Interactive Atom Displays!

Hey there! Welcome to this project. Ever wanted to feel like Tony Stark, interacting with complex UIs just by moving your hands? Well, you're in the right place! This little project brings that sci-fi dream a bit closer to reality.

We've got two main interactive displays here – one for an Arc Reactor core and another for visualizing subatomic particles – both controlled in real-time by your hand movements via your webcam. Pretty neat, huh?





## How it Works 

This project has three core pieces that talk to each other to make the magic happen:

1.  **`app.py` (The Brains - Python Backend)**
    *   This is where the real-time hand tracking lives. It uses `mediapipe` to detect your hand, figure out its position, how "pinched" your fingers are (think zooming in!), and even its 3D rotation.
    *   It then takes all that juicy data and broadcasts it over a `websockets` connection.
    *   **What you need:** Python 3, `opencv-python`, `mediapipe`, `websockets`.

2.  **`suit.html` (The Arc Reactor - Frontend Display)**
    *   This is your personal Arc Reactor HUD! It's a web page that connects to the Python backend.
    *   It uses `three.js` to render a cool, dynamic 3D Arc Reactor model.
    *   Your hand movements directly control the reactor's position, scale (pinch!), and rotation. You can even cycle through different "core elements" by moving your hand left or right on the screen.
    *   **What you need:** Just a modern web browser!

3.  **`index.html` (The Subatomic Explorer - Another Frontend Display)**
    *   Think of this as your window into the microscopic world. Similar to `suit.html`, it's a web page that talks to `app.py`.
    *   It also uses `three.js` to display a mesmerizing 3D atom model.
    *   Your hand gestures manipulate the atom's movement, size, and orientation. Swipe left or right to switch between different elements (Hydrogen, Helium, Lithium, Carbon).
    *   **What you need:** Again, just a modern web browser!

## Getting Started (Let's Get This Running!)

### 1. Set up the Python Backend (`app.py`)

First things first, you need to get the hand tracking server up and running.

*   **Install Dependencies:**
    If you don't have them already, open your terminal or command prompt and run:
    ```bash
    pip install opencv-python mediapipe websockets
    ```
*   **Run the Server:**
    Navigate to the directory where you saved `app.py` and execute:
    ```bash
    python app.py
    ```
    You should see a message like "Server started on ws://localhost:8765". This means it's ready to go! Leave this terminal window open.

### 2. Launch the Frontend Displays

Now that the backend is listening, you can open the interactive displays.

*   **Open `suit.html`:**
    Just double-click on the `suit.html` file in your browser, or open it directly in your browser.
*   **Open `index.html`:**
    Do the same for `index.html`. You can have both open at the same time in different tabs or windows!

**Important Note:** When you open the HTML files, your browser will likely ask for permission to use your webcam. You *must* allow it for the hand tracking to work.

## How to Interact 

Once everything's running and your webcam is active, try these gestures:

*   **Move Your Hand:** The 3D model (Arc Reactor or Atom) will follow your hand's X and Y position on the screen.
*   **Pinch Your Fingers:** Bring your thumb and index finger together (like you're pinching something). The model will scale up, giving the impression of "powering up" or "zooming in"!
*   **Rotate Your Hand:** Twist your wrist and hand, and watch the 3D model rotate in sync.
*   **Swipe Left/Right (for element/core changes):** Move your hand to the far left or far right of the camera view to cycle through the different core types in `suit.html` or elements in `index.html`.

## Built With

*   [Python](https://www.python.org/) - For the backend logic.
*   [MediaPipe Hands](https://developers.google.com/mediapipe/solutions/vision/hand_landmarker) - For robust hand tracking.
*   [Websockets](https://websockets.readthedocs.io/en/stable/) - For real-time communication between Python and the browser.
*   [Three.js](https://threejs.org/) - For beautiful 3D rendering in the browser.
*   [HTML/CSS/JavaScript](https://developer.mozilla.org/en-US/docs/Web) - The foundation of the web interfaces.

---

Feel free to poke around, experiment, and maybe even add your own custom elements or reactor designs! Enjoy playing around with your new, futuristic HUD!
</code></pre>
