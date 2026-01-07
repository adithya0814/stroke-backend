from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import inch

def create_pdf(filename):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontSize=24,
        spaceAfter=30,
        alignment=1  # Center
    )
    story.append(Paragraph("Stroke Recovery Prediction System - Project Overview", title_style))
    story.append(Spacer(1, 12))

    # Project Summary
    story.append(Paragraph("Project Summary", styles['Heading2']))
    summary_text = """
    This is a comprehensive full-stack web application designed to predict stroke recovery progress using multimodal behavioral data. The system collects and analyzes keystroke dynamics, mouse movements, and body pose from webcam footage to assess motor and cognitive recovery in stroke patients. It provides personalized recovery scores, generates detailed PDF reports, and maintains a history of assessment sessions. The application is built for healthcare professionals or patients to monitor rehabilitation progress objectively, combining machine learning predictions with a user-friendly interface for data collection and visualization.
    """
    story.append(Paragraph(summary_text, styles['Normal']))
    story.append(Spacer(1, 12))

    # Tech Stack
    story.append(Paragraph("Tech Stack and Explanations", styles['Heading2']))
    story.append(Paragraph("The project uses a modern tech stack with separation between backend (API and ML models) and frontend (user interface). Here's a breakdown:", styles['Normal']))

    story.append(Paragraph("Backend (Python-based API and ML processing)", styles['Heading3']))
    backend_items = [
        "FastAPI: A high-performance, asynchronous web framework for building REST APIs. Used for handling HTTP requests, authentication, and serving predictions. It's chosen for its speed, automatic API documentation (Swagger), and type safety with Pydantic models.",
        "MongoDB (via Motor): A NoSQL database for storing user accounts, authentication data, and session histories. Motor is the async MongoDB driver compatible with FastAPI's async nature.",
        "JWT (JSON Web Tokens): For secure user authentication and session management, ensuring only authorized users can access predictions and history.",
        "Scikit-learn and XGBoost: Machine learning libraries for training and deploying predictive models. Scikit-learn handles preprocessing and simpler models, while XGBoost provides gradient boosting for complex predictions (e.g., webcam pose analysis).",
        "Joblib: For serializing and loading trained ML models (e.g., keystroke.joblib, dragdrop_model.joblib), allowing efficient model deployment without retraining.",
        "MediaPipe: Google's ML framework for real-time pose estimation from webcam video. Extracts joint angles, speeds, and smoothness metrics for upper-body movement analysis.",
        "NumPy and Pandas: For numerical computations and data manipulation in ML pipelines.",
        "Python-dotenv: For managing environment variables (e.g., database URLs, secrets).",
        "Uvicorn: ASGI server for running the FastAPI app in development."
    ]
    for item in backend_items:
        story.append(Paragraph(f"• {item}", styles['Normal']))

    story.append(Paragraph("Frontend (React-based UI)", styles['Heading3']))
    frontend_items = [
        "React: A component-based JavaScript library for building dynamic user interfaces. Handles state management, routing, and real-time data collection.",
        "Vite: A fast build tool and development server for React apps, providing hot module replacement and optimized bundling.",
        "Tailwind CSS: A utility-first CSS framework for rapid, responsive styling without writing custom CSS. Used for consistent, modern UI design.",
        "Material UI (MUI): A React component library providing pre-built UI elements like buttons, steppers, and cards. Ensures a professional, accessible interface.",
        "React Router: For client-side routing between pages (e.g., login, dashboard, home).",
        "Axios: A promise-based HTTP client for making API calls to the backend (e.g., sending collected data for predictions).",
        "React Webcam: A library for accessing the user's webcam in the browser, enabling real-time video capture for pose analysis.",
        "MediaPipe (integrated via JavaScript SDK): For client-side pose detection, processing video frames to extract features before sending to the backend.",
        "Framer Motion: An animation library for smooth transitions and interactive effects (e.g., step progress animations).",
        "React PDF Renderer: For generating downloadable PDF reports directly in the browser from prediction data.",
        "Recharts: A charting library for visualizing recovery scores and trends in the dashboard.",
        "File Saver: For downloading generated PDFs.",
        "ESLint and PostCSS: For code linting and CSS processing (e.g., autoprefixing for Tailwind)."
    ]
    for item in frontend_items:
        story.append(Paragraph(f"• {item}", styles['Normal']))

    story.append(Paragraph("The stack emphasizes performance, scalability, and ease of development: Python for robust ML and API handling, React for interactive UIs, and cloud-ready deployment (e.g., via Render as seen in render.yaml).", styles['Normal']))
    story.append(Spacer(1, 12))

    # Work of the Project
    story.append(Paragraph("Work of the Project (Point-wise)", styles['Heading2']))
    work_items = [
        "1. User Authentication and Authorization: Implements signup/signin with JWT tokens stored in localStorage. Protects routes and API endpoints to ensure secure access.",
        "2. Session Management: Stores user sessions in MongoDB, including prediction results, timestamps, and PDF filenames. Allows retrieval of session history for tracking progress over time.",
        "3. Keystroke Data Collection: Provides a typing test interface where users type a passage. Captures metrics like typing speed (WPM/CPM), dwell time, flight time, errors, and consistency using JavaScript event listeners.",
        "4. Mouse Movement Data Collection: Includes a drag-and-drop task (e.g., moving objects on screen). Tracks metrics like distance error, time taken, path efficiency, jerkiness, and aiming accuracy via mouse event handlers.",
        "5. Webcam Pose Analysis: Uses MediaPipe to detect upper-body poses in real-time video. Extracts features such as elbow/shoulder angles, speeds, velocities, and smoothness for left/right arms.",
        "6. Individual Model Predictions: Sends collected features to backend ML models: Keystroke model (Scikit-learn): Predicts recovery score based on typing dynamics. Mouse model (Scikit-learn): Combines keystroke and mouse features for drag-and-drop prediction. Webcam model (XGBoost): Analyzes pose features for motor recovery assessment, including classification (e.g., \"excellent\" recovery).",
        "7. Combined Prediction: Aggregates scores from all modalities into a final recovery score and category (e.g., \"good\", \"average\"). Handles partial data (e.g., if webcam is skipped).",
        "8. PDF Report Generation: Creates detailed reports using React PDF Renderer, including scores, charts, and recommendations. Uploads PDFs to the backend for storage and download.",
        "9. Dashboard and UI Workflow: Features a stepper-based interface guiding users through data collection steps. Displays results in cards, charts, and history tables. Includes sidebar navigation and logout functionality.",
        "10. Data Storage and Retrieval: Saves predictions and reports in MongoDB. Provides endpoints for fetching session history and downloading PDFs.",
        "11. Error Handling and Validation: Implements try-catch blocks, input validation (e.g., via Pydantic), and user feedback for failed predictions or missing data.",
        "12. Deployment Readiness: Configured for cloud deployment (e.g., Render) with environment variables, CORS handling, and build scripts for both backend and frontend."
    ]
    for item in work_items:
        story.append(Paragraph(item, styles['Normal']))

    story.append(Spacer(1, 12))

    # Algorithms
    story.append(Paragraph("Algorithms Used in the Project", styles['Heading2']))
    story.append(Paragraph("The project employs machine learning algorithms for predicting stroke recovery based on multimodal data (keystroke dynamics, mouse movements, and webcam pose analysis). Below is a detailed breakdown of the algorithms used, based on inspection of the trained models and code:", styles['Normal']))

    story.append(Paragraph("1. Keystroke Prediction Model", styles['Heading3']))
    keystroke_items = [
        "• Algorithm: Random Forest Regressor (from scikit-learn's sklearn.ensemble.RandomForestRegressor).",
        "• Purpose: Predicts a continuous recovery score based on typing features (e.g., typing speed, dwell time, errors, consistency).",
        "• How it Works: An ensemble method that builds multiple decision trees and averages their predictions to reduce overfitting. It handles non-linear relationships in keystroke data effectively.",
        "• Implementation: Loaded from backend/models/keystroke.joblib. Features are preprocessed and fed into the model for regression output."
    ]
    for item in keystroke_items:
        story.append(Paragraph(item, styles['Normal']))

    story.append(Paragraph("2. Mouse Movement Prediction Model", styles['Heading3']))
    mouse_items = [
        "• Algorithm: XGBoost Classifier (from xgboost.sklearn.XGBClassifier).",
        "• Purpose: Classifies recovery level based on combined keystroke and mouse features (e.g., distance error, path efficiency, jerkiness from drag-and-drop tasks).",
        "• How it Works: A gradient boosting algorithm that iteratively builds decision trees, optimizing for classification accuracy. It excels in handling tabular data with mixed features and provides feature importance insights.",
        "• Implementation: Loaded from backend/models/dragdrop_model.joblib. Outputs a categorical prediction (e.g., recovery class)."
    ]
    for item in mouse_items:
        story.append(Paragraph(item, styles['Normal']))

    story.append(Paragraph("3. Webcam Pose Analysis Models", styles['Heading3']))
    webcam_items = [
        "• Algorithms: XGBoost (both Classifier and Regressor, wrapped in scikit-learn Pipelines).",
        "  - Classifier: XGBoost Classifier for predicting recovery categories (e.g., \"excellent\", \"good\").",
        "  - Regressor: XGBoost Regressor for predicting continuous recovery scores.",
        "• Purpose: Analyzes upper-body pose features (e.g., elbow/shoulder angles, speeds, smoothness) extracted from webcam video to assess motor recovery.",
        "• How it Works: Gradient boosting for high-performance predictions on complex, high-dimensional pose data. Pipelines include preprocessing (e.g., StandardScaler for feature normalization) before XGBoost.",
        "• Implementation: Loaded from backend/models/recovery_model_xgb_both.pkl (classifier) and backend/models/recovery_regressor_both.pkl (regressor). Features are derived from MediaPipe's pose estimation."
    ]
    for item in webcam_items:
        story.append(Paragraph(item, styles['Normal']))

    story.append(Paragraph("4. Pose Estimation (Underlying for Webcam)", styles['Heading3']))
    pose_items = [
        "• Algorithm: MediaPipe's BlazePose (deep learning-based pose estimation model).",
        "• Purpose: Detects and tracks human body keypoints (joints) in real-time from webcam video to extract features like angles, velocities, and smoothness.",
        "• How it Works: Uses convolutional neural networks (CNNs) trained on large datasets for accurate, low-latency pose detection. Processes video frames to output 3D joint positions, which are then analyzed for recovery metrics.",
        "• Implementation: Integrated via MediaPipe's JavaScript SDK in the frontend (WebcamPanel.jsx) and Python SDK in the backend (pose_analysis.py). Features are computed from keypoints (e.g., left/right elbow and shoulder angles)."
    ]
    for item in pose_items:
        story.append(Paragraph(item, styles['Normal']))

    story.append(Paragraph("Additional Notes: All models use feature scaling (e.g., StandardScaler in pipelines) and custom feature engineering (e.g., angle calculations from pose keypoints). No advanced algorithms like neural networks are used beyond MediaPipe's pre-trained models. Model Training: The models appear to be pre-trained (joblib files), likely using historical stroke patient data. The project focuses on inference/deployment rather than training. Ensemble and Aggregation: Individual model scores are averaged for the final prediction, with simple thresholding for categories (e.g., score >= 80 → \"excellent\"). Why These Algorithms?: Random Forest and XGBoost are chosen for their robustness, interpretability, and performance on tabular/structured data. MediaPipe provides efficient, real-time pose analysis without requiring custom deep learning training.", styles['Normal']))

    doc.build(story)

if __name__ == "__main__":
    create_pdf("ProjectSummary.pdf")