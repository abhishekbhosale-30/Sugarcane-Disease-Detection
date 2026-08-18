import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageStat
from pathlib import Path
from datetime import datetime
from io import BytesIO


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Sugarcane AI Disease Detection",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# PAGE ROUTING
# ============================================================
# The custom navbar uses normal HTML links. These query parameters
# are converted into real Streamlit page navigation here.
_requested_page = st.query_params.get("page")

if _requested_page == "about":
    st.switch_page("pages/About_Us.py")

if _requested_page == "how_it_works":
    st.switch_page("pages/How_It_Works.py")


# ============================================================
# MODEL PATH
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = (
    BASE_DIR
    / "runs"
    / "classify"
    / "sugarcane_disease_model"
    / "weights"
    / "best.pt"
)


# ============================================================
# CHECK MODEL
# ============================================================

if not MODEL_PATH.exists():

    st.error("❌ Model file not found.")

    st.code(str(MODEL_PATH))

    st.stop()


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    return YOLO(str(MODEL_PATH))


model = load_model()


# ============================================================
# COMPLETE CSS
# ============================================================

st.html("""
<style>

/* ============================================================
   GENERAL PAGE
   ============================================================ */

.stApp {

    background: #F3F7F4;
}

.block-container {

    max-width: 1250px;

    padding-top: 18px;

    padding-bottom: 90px;
}


/* ============================================================
   CUSTOM NAVIGATION BAR
   Desktop:
   🌿 Sugarcane AI | Home | About Us | How It Works | English ▾

   Mobile:
   🌿 Sugarcane AI | ☰
   and the hamburger contains Home, About Us, How It Works,
   and Language.
   ============================================================ */

.custom-navbar {
    width: 100%;
    margin-top: 60px;
    background: #14532D;
    border-radius: 12px;
    padding: 12px 20px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    box-sizing: border-box;
    margin-bottom: 0;
    box-shadow: 0 4px 12px rgba(20, 83, 45, 0.12);
}

/* Logo */
.nav-logo {
    display: flex;
    align-items: center;
    color: #FFFFFF;
    font-size: 17px;
    font-weight: 800;
    white-space: nowrap;
}

/* Desktop links */
.desktop-nav {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    flex: 1;
    margin-left: 20px;
}

.nav-link {
    display: inline-block;
    color: #DCFCE7 !important;
    text-decoration: none !important;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 12px;
    border-radius: 7px;
    transition: 0.2s ease;
    white-space: nowrap;
}

.nav-link:hover {
    background: #166534;
    color: #FFFFFF !important;
}

/* Desktop language */
.desktop-language {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    position: relative;
}

.language-menu {
    position: relative;
}

.language-menu summary {
    list-style: none;
    cursor: pointer;
    color: #DCFCE7;
    font-size: 13px;
    font-weight: 600;
    padding: 8px 10px;
    white-space: nowrap;
}

.language-menu summary::-webkit-details-marker {
    display: none;
}

.language-menu summary:hover {
    color: #FFFFFF;
}

.language-options {
    position: absolute;
    right: 0;
    top: 38px;
    z-index: 99999;
    min-width: 120px;
    background: #14532D;
    border: 1px solid rgba(220, 252, 231, 0.25);
    border-radius: 9px;
    padding: 5px;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.18);
}

.language-options a {
    display: block;
    color: #DCFCE7 !important;
    text-decoration: none !important;
    padding: 8px 10px;
    border-radius: 6px;
    font-size: 12px;
    font-weight: 600;
}

.language-options a:hover {
    background: #166534;
    color: #FFFFFF !important;
}

/* Mobile navbar */
.mobile-navbar {
    display: none;
}

.mobile-menu {
    position: relative;
}

.mobile-menu summary {
    list-style: none;
    cursor: pointer;
    color: #DCFCE7;
    font-size: 28px;
    font-weight: 800;
    line-height: 1;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    user-select: none;
}

.mobile-menu summary::-webkit-details-marker {
    display: none;
}

.mobile-menu summary::marker {
    display: none;
}

.mobile-menu[open] summary {
    color: #FFFFFF;
}

.mobile-menu-content {
    position: absolute;
    right: 0;
    top: 50px;
    z-index: 99999;
    width: 220px;
    background: #14532D;
    border: 1px solid rgba(220, 252, 231, 0.25);
    border-radius: 12px;
    padding: 8px;
    box-shadow: 0 10px 25px rgba(0, 0, 0, 0.20);
}

.mobile-menu-content .nav-link {
    display: block;
    width: 100%;
    box-sizing: border-box;
    padding: 11px 12px;
    font-size: 13px;
    color: #DCFCE7 !important;
}

.mobile-menu-content .nav-link:hover {
    background: #166534;
    color: #FFFFFF !important;
}

.mobile-language-title {
    color: #DCFCE7;
    font-size: 11px;
    font-weight: 700;
    padding: 11px 12px 6px;
}

.mobile-language-options {
    display: flex;
    gap: 6px;
    padding: 0 6px 6px;
}

.mobile-language-options a {
    flex: 1;
    text-align: center;
    color: #DCFCE7 !important;
    text-decoration: none !important;
    padding: 9px 5px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    background: transparent;
}

.mobile-language-options a:hover {
    background: #166534;
    color: #FFFFFF !important;
}

/* Mobile: logo + hamburger are forced into ONE HTML flex row */
/* ============================================================
   RESULT STATUS / PDF REPORT
   ============================================================ */

.confidence-status {
    margin-top: 10px;
    padding: 9px 12px;
    border-radius: 9px;
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    color: #166534;
    font-size: 12px;
    font-weight: 800;
}

.low-confidence-card {
    margin-top: 12px;
    background: #FFF7ED;
    border: 1px solid #FED7AA;
    border-left: 4px solid #EA580C;
    border-radius: 10px;
    padding: 13px;
    color: #9A3412;
    font-size: 12px;
    line-height: 1.55;
}

.overview-card {
    margin-top: 14px;
    background: #F0FDF4;
    border: 1px solid #BBF7D0;
    border-radius: 11px;
    padding: 14px;
}

.overview-title {
    color: #14532D;
    font-size: 14px;
    font-weight: 800;
    margin-bottom: 6px;
}

.overview-text {
    color: #475569;
    font-size: 12px;
    line-height: 1.6;
}

.report-box {
    margin-top: 16px;
    background: #FFFFFF;
    border: 1px solid #DDE7E0;
    border-radius: 12px;
    padding: 14px;
}

.report-title {
    color: #14532D;
    font-size: 15px;
    font-weight: 800;
}

@media (max-width: 768px) {

    .custom-navbar {
        width: 100%;
        margin-top: 50px;
        padding: 0 16px;
        min-height: 64px;
        border-radius: 0 35px;
        box-sizing: border-box;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }

    .desktop-navbar {
        display: none !important;
    }

    .mobile-navbar {
        display: flex !important;
        align-items: center !important;
        justify-content: space-between !important;
        width: 100% !important;
        min-height: 64px !important;
    }

    .mobile-navbar .nav-logo {
        display: flex !important;
        align-items: center !important;
        color: #FFFFFF !important;
        font-size: 16px !important;
        font-weight: 800 !important;
        white-space: nowrap !important;
        min-width: 0 !important;
    }

    .mobile-navbar .mobile-menu {
        display: block !important;
        flex: 0 0 auto !important;
    }

    .mobile-navbar .mobile-menu summary {
        width: 42px !important;
        height: 42px !important;
        font-size: 28px !important;
    }

    /* Keep the existing page mobile layout below navbar */
    .project-header {
        padding: 20px;
        margin-top: 30px;
        margin-bottom: 20px;
        border-radius: 0 35px;
    }

    .header-title {
        font-size: 22px;
    }

    .header-subtitle {
        font-size: 12px;
    }
}

/* ============================================================
   PROJECT HEADER
   ============================================================ */

.project-header {

    background: #14532D;

    border-radius: 0px 50px;

    padding: 25px 30px;

    margin-top: 50px;

    margin-bottom: 30px;

    box-shadow:
        0 5px 18px rgba(20, 83, 45, 0.12);
}


.header-title {

    color: #FFFFFF;

    font-size: 30px;

    font-weight: 800;

    line-height: 1.25;

    margin: 0 0 10px 0;
}


.header-subtitle {

    color: #DCFCE7;

    font-size: 14px;

    font-weight: 500;

    line-height: 1.5;

    margin: 0;
}


/* ============================================================
   MAIN PANEL
   ============================================================ */

.main-panel {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 16px;

    padding: 20px;

    box-shadow:
        0 4px 16px rgba(20, 83, 45, 0.07);
}


.panel-title {

    color: #14532D;

    font-size: 20px;

    font-weight: 800;

    line-height: 1.3;
}


.panel-subtitle {

    color: #64748B;

    font-size: 13px;

    line-height: 1.5;

    margin-top: 5px;
}


/* ============================================================
   UPLOAD INFO
   ============================================================ */

.upload-info {

    background: #F0FDF4;

    border: 1px solid #BBF7D0;

    border-radius: 10px;

    padding: 13px;

    margin-top: 12px;

    color: #166534;

    font-size: 13px;

    line-height: 1.5;
}


/* ============================================================
   WAITING CARD
   ============================================================ */

.waiting {

    background: #F8FAFC;

    border: 1px dashed #CBD5E1;

    border-radius: 13px;

    padding: 45px 20px;

    text-align: center;

    margin-top: 15px;
}


.waiting-icon {

    font-size: 38px;
}


.waiting-title {

    color: #334155;

    font-size: 20px;

    font-weight: 700;

    margin-top: 8px;
}


.waiting-text {

    color: #64748B;

    font-size: 13px;

    margin-top: 6px;
}


/* ============================================================
   PREDICTED DISEASE + CONFIDENCE
   ONE DIV
   ============================================================ */

.prediction-summary {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 15px;

    background: #F0FDF4;

    border: 1px solid #BBF7D0;

    border-radius: 13px;

    padding: 17px;

    margin-top: 15px;
}


.summary-item {

    display: flex;

    flex-direction: column;

    justify-content: center;

    gap: 6px;
}


.summary-label {

    color: #64748B;

    font-size: 11px;

    font-weight: 800;

    letter-spacing: 0.5px;

    text-transform: uppercase;
}


.summary-value {

    color: #14532D;

    font-size: 21px;

    font-weight: 800;
}


/* ============================================================
   CONFIDENCE BAR
   ============================================================ */

.confidence-bar {

    width: 100%;

    height: 7px;

    background: #DDE7E0;

    border-radius: 20px;

    overflow: hidden;

    margin-top: 10px;
}


.confidence-fill {

    height: 100%;

    background: #16A34A;

    border-radius: 20px;
}


/* ============================================================
   SECTION HEADINGS
   ============================================================ */

.probability-heading,
.information-heading {

    color: #14532D;

    font-size: 19px;

    font-weight: 800;

    margin-top: 22px;

    margin-bottom: 3px;
}


.probability-subheading,
.information-subheading {

    color: #64748B;

    font-size: 12px;

    margin-bottom: 10px;
}


/* ============================================================
   PROBABILITY GRID
   ============================================================ */

.probability-grid {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 10px;

    margin-top: 12px;
}


/* ============================================================
   PROBABILITY CARD
   ============================================================ */

.probability-card {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 11px;

    padding: 12px;

    min-width: 0;
}


/*
   If there are 5 classes,
   fifth class takes full width.
*/

.probability-card:last-child:nth-child(odd) {

    grid-column: 1 / -1;
}


.probability-card-top {

    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 8px;

    margin-bottom: 8px;
}


.probability-name {

    display: flex;

    align-items: center;

    gap: 6px;

    color: #334155;

    font-size: 13px;

    font-weight: 700;
}


.probability-icon {

    font-size: 15px;
}


.probability-value {

    font-size: 13px;

    font-weight: 800;
}


/* ============================================================
   PROBABILITY BAR
   ============================================================ */

.probability-track {

    width: 100%;

    height: 6px;

    background: #E8EEF0;

    border-radius: 20px;

    overflow: hidden;
}


.probability-fill {

    height: 100%;

    min-width: 2px;

    border-radius: 20px;
}


.probability-status {

    color: #94A3B8;

    font-size: 10px;

    margin-top: 6px;
}


/* ============================================================
   INFORMATION 2 x 2 GRID
   ============================================================ */

.info-grid {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 10px;

    margin-top: 12px;
}


/* ============================================================
   INFORMATION CARD
   ============================================================ */

.info {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-left: 4px solid #16A34A;

    border-radius: 10px;

    padding: 13px;

    min-height: 125px;

    box-sizing: border-box;
}


.info-title {

    color: #14532D;

    font-size: 13px;

    font-weight: 800;

    margin-bottom: 6px;
}


.info-text {

    color: #475569;

    font-size: 12px;

    line-height: 1.55;
}


/* ============================================================
   BUTTON
   ============================================================ */

.stButton > button {

    background: #15803D;

    color: #FFFFFF;

    border: none;

    border-radius: 9px;

    min-height: 45px;

    font-size: 15px;

    font-weight: 700;
}


.stButton > button:hover {

    background: #166534;

    color: #FFFFFF;

    border: none;
}


/* ============================================================
   RIGHT SIDE SCROLL
   ============================================================ */

div[data-testid="stHorizontalBlock"]
> div[data-testid="column"]:nth-child(2) {

    max-height: calc(100vh - 205px);

    overflow-y: auto;

    padding-right: 10px;
}


/* SCROLLBAR */

div[data-testid="stHorizontalBlock"]
> div[data-testid="column"]:nth-child(2)::-webkit-scrollbar {

    width: 7px;
}


div[data-testid="stHorizontalBlock"]
> div[data-testid="column"]:nth-child(2)::-webkit-scrollbar-track {

    background: #E8F1EB;

    border-radius: 10px;
}


div[data-testid="stHorizontalBlock"]
> div[data-testid="column"]:nth-child(2)::-webkit-scrollbar-thumb {

    background: #15803D;

    border-radius: 10px;
}


/* ============================================================
   FOOTER
   ============================================================ */

.project-footer {

    position: fixed;

    left: 0;

    bottom: 0;

    width: 100%;

    z-index: 9999;

    background: #123B27;

    color: #DCFCE7;

    text-align: center;

    padding: 11px 10px;

    font-size: 12px;

    border-top: 2px solid #22C55E;

    box-shadow:
        0 -3px 12px rgba(0, 0, 0, 0.08);
}


/* ============================================================
   MOBILE RESPONSIVE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {

        padding-left: 10px;

        padding-right: 10px;

        padding-top: 12px;

        padding-bottom: 75px;
    }


    /* NAVBAR */

    .custom-navbar {

        padding: 10px 12px;

        border-radius: 10px;
    }


    .nav-logo {

        font-size: 13px;
    }


    .nav-links {

        gap: 2px;
    }


    .nav-link {

        font-size: 9px;

        padding: 6px 6px;
    }


    /* PROJECT HEADER */

    .project-header {

        padding: 20px;

        margin-top: 30px;

        margin-bottom: 20px;

        border-radius: 0px 35px;
    }


    .header-title {

        font-size: 22px;
    }


    .header-subtitle {

        font-size: 12px;
    }


    /* COLUMNS */

    div[data-testid="stHorizontalBlock"] {

        flex-direction: column;

        gap: 15px;
    }


    div[data-testid="stHorizontalBlock"]
    > div[data-testid="column"] {

        width: 100% !important;
    }


    /* RIGHT SIDE */

    div[data-testid="stHorizontalBlock"]
    > div[data-testid="column"]:nth-child(2) {

        max-height: none;

        overflow-y: visible;

        padding-right: 0;
    }


    /* MAIN PANEL */

    .main-panel {

        padding: 16px;

        border-radius: 14px;
    }


    /* PREDICTION SUMMARY
       STILL TWO COLUMNS
    */

    .prediction-summary {

        grid-template-columns: 1fr 1fr;

        gap: 8px;

        padding: 12px;
    }


    .summary-label {

        font-size: 9px;
    }


    .summary-value {

        font-size: 15px;

        word-break: break-word;
    }


    /* PROBABILITY
       STILL 2 COLUMNS
    */

    .probability-grid {

        grid-template-columns: 1fr 1fr;

        gap: 7px;
    }


    .probability-card {

        padding: 9px;
    }


    .probability-name {

        font-size: 10px;
    }


    .probability-value {

        font-size: 10px;
    }


    .probability-status {

        font-size: 8px;
    }


    /* INFORMATION
       STILL 2 x 2
    */

    .info-grid {

        grid-template-columns: 1fr 1fr;

        gap: 7px;
    }


    .info {

        min-height: 125px;

        padding: 10px;
    }


    .info-title {

        font-size: 10px;
    }


    .info-text {

        font-size: 9px;

        line-height: 1.45;
    }


    /* FOOTER */

    .project-footer {

        font-size: 9px;

        padding: 9px 5px;
    }

}



""")

# ============================================================
# LANGUAGE TEXT
# ============================================================

english = {
    "home": "Home",
    "about": "About",
    "how_it_works": "How It Works",
    "language_label": "🌐 Language",
    "title": "🌿 Sugarcane AI Disease Detection",
    "subtitle": "AI-powered classification of sugarcane leaf diseases",
    "upload_title": "📤 Upload Leaf Image",
    "upload_subtitle": "Upload a clear sugarcane leaf image for AI-based disease classification.",
    "choose_image": "Choose a sugarcane leaf image",
    "uploaded_caption": "Uploaded Sugarcane Leaf",
    "upload_success": "✓ Image uploaded successfully",
    "upload_ready": "Your image is ready for AI analysis.",
    "supported_formats": "📷 Supported Formats",
    "tip": "💡 Tip",
    "tip_text": "Use a clear sugarcane leaf image with good lighting.",
    "predict": "🔍 Predict Disease",
    "result_title": "📊 Prediction Result",
    "result_subtitle": "AI model prediction and confidence analysis.",
    "waiting_title": "Waiting for Image",
    "waiting_text": "Upload a sugarcane leaf image to start disease prediction.",
    "ready_title": "Ready to Analyze",
    "ready_text": "Your image is ready. Click Predict Disease to start.",
    "predicted_disease": "Predicted Disease",
    "confidence": "Confidence",
    "probability_title": "📊 Disease Probability Analysis",
    "probability_subtitle": "Confidence distribution across all trained classes",
    "most_likely": "Most likely",
    "possible": "Possible",
    "low_probability": "Low probability",
    "information_title": "🌱 Disease Information",
    "information_subtitle": "Important information about the predicted condition",
    "symptoms": "🔎 Symptoms",
    "prevention": "🛡️ Prevention",
    "recommendation": "💡 Recommendation",
    "management": "🧪 Management",
    "analyzing": "Analyzing sugarcane leaf...",

        "confidence_high":
            "High Confidence",

        "confidence_medium":
            "Moderate Confidence",

        "confidence_low":
            "Low Confidence",

        "low_confidence_message":
            "The model is not sufficiently confident about this image. Please upload a clearer sugarcane leaf image.",

        "overview_title":
            "Disease Overview",

        "download_title":
            "Download Disease Report",

        "download_report":
            "Download PDF Report",

    "invalid_image": "Unable to open this image. Please upload a valid JPG, JPEG or PNG image.",
    "prediction_failed": "❌ Prediction failed.",
    "footer": "🌿 Sugarcane AI Disease Detection | YOLO Classification Model | Research Project",
}

marathi = {
    "home": "मुख्यपृष्ठ",
    "about": "माहिती",
    "how_it_works": "कार्यपद्धती",
    "language_label": "🌐 भाषा",
    "title": "🌿 Sugarcane AI Disease Detection",
    "subtitle": "ऊसाच्या पानावरील रोगांचे AI आधारित वर्गीकरण",
    "upload_title": "📤 पानाचा फोटो अपलोड करा",
    "upload_subtitle": "रोगाचे AI आधारित निदान करण्यासाठी ऊसाच्या पानाचा स्पष्ट फोटो अपलोड करा.",
    "choose_image": "ऊसाच्या पानाचा फोटो निवडा",
    "uploaded_caption": "अपलोड केलेला ऊसाच्या पानाचा फोटो",
    "upload_success": "✓ फोटो यशस्वीरित्या अपलोड झाला",
    "upload_ready": "तुमचा फोटो AI विश्लेषणासाठी तयार आहे.",
    "supported_formats": "📷 समर्थित फोटो प्रकार",
    "tip": "💡 सूचना",
    "tip_text": "चांगल्या प्रकाशात घेतलेला ऊसाच्या पानाचा स्पष्ट फोटो वापरा.",
    "predict": "🔍 रोगाचे निदान करा",
    "result_title": "📊 रोग निदानाचा निकाल",
    "result_subtitle": "AI मॉडेलद्वारे रोगाचे निदान आणि अचूकता.",
    "waiting_title": "फोटोची प्रतीक्षा आहे",
    "waiting_text": "रोगाचे निदान सुरू करण्यासाठी ऊसाच्या पानाचा फोटो अपलोड करा.",
    "ready_title": "फोटो विश्लेषणासाठी तयार आहे",
    "ready_text": "तुमचा फोटो तयार आहे. निदान सुरू करण्यासाठी बटण दाबा.",
    "predicted_disease": "अंदाजित रोग",
    "confidence": "अचूकता",
    "probability_title": "📊 रोगाच्या संभाव्यतेचे विश्लेषण",
    "probability_subtitle": "सर्व प्रशिक्षित रोग वर्गांमधील संभाव्यतेचे वितरण",
    "most_likely": "सर्वाधिक शक्यता",
    "possible": "संभाव्य",
    "low_probability": "कमी शक्यता",
    "information_title": "🌱 रोगाची माहिती",
    "information_subtitle": "अंदाजित रोगाविषयी महत्त्वाची माहिती",
    "symptoms": "🔎 लक्षणे",
    "prevention": "🛡️ प्रतिबंध",
    "recommendation": "💡 शिफारस",
    "management": "🧪 व्यवस्थापन",
    "analyzing": "ऊसाच्या पानाचे विश्लेषण सुरू आहे...",

        "confidence_high":
            "उच्च विश्वास पातळी",

        "confidence_medium":
            "मध्यम विश्वास पातळी",

        "confidence_low":
            "कमी विश्वास पातळी",

        "low_confidence_message":
            "मॉडेलला या प्रतिमेबद्दल पुरेसा विश्वास नाही. अधिक स्पष्ट ऊसाच्या पानाची प्रतिमा अपलोड करा.",

        "overview_title":
            "रोगाची थोडक्यात माहिती",

        "download_title":
            "रोगाचा अहवाल डाउनलोड करा",

        "download_report":
            "PDF अहवाल डाउनलोड करा",

    "invalid_image": "फोटो उघडता आला नाही. कृपया JPG, JPEG किंवा PNG फोटो अपलोड करा.",
    "prediction_failed": "❌ रोगाचे निदान करण्यात समस्या आली.",
    "footer": "🌿 Sugarcane AI Disease Detection | YOLO Classification Model | Research Project",
}


# ============================================================
# DISEASE OVERVIEW
# ============================================================

overview_info = {

    "Healthy": {
        "English":
            "The uploaded leaf appears healthy according to the model prediction and does not show the main visual patterns represented by the trained disease classes.",
        "Marathi":
            "मॉडेलच्या अंदाजानुसार अपलोड केलेले पान निरोगी दिसते आणि प्रशिक्षित रोग वर्गांमधील प्रमुख दृश्य लक्षणे दिसून येत नाहीत."
    },

    "Mosaic": {
        "English":
            "Mosaic is associated with characteristic light and dark green patterns or mosaic-like discoloration on sugarcane leaves.",
        "Marathi":
            "मोज़ेक रोगामध्ये ऊसाच्या पानांवर फिकट आणि गडद हिरव्या रंगाचे पट्टे किंवा मोझेकसारखा रंगाचा नमुना दिसू शकतो."
    },

    "RedRot": {
        "English":
            "Red rot is a serious sugarcane disease that can cause reddish or reddish-brown discoloration in affected plant tissues.",
        "Marathi":
            "लाल कुज रोग हा ऊसातील महत्त्वाचा रोग असून रोगग्रस्त भागात लालसर किंवा लाल-तपकिरी रंगाचे बदल आणि कुजण्याची लक्षणे दिसू शकतात."
    },

    "Rust": {
        "English":
            "Rust can produce rust-colored spots or lesions on sugarcane leaves and should be monitored regularly.",
        "Marathi":
            "तांबेरा रोगामध्ये ऊसाच्या पानांवर तांबूस-तपकिरी ठिपके किंवा डाग दिसू शकतात आणि पिकाची नियमित तपासणी करणे आवश्यक आहे."
    },

    "Yellow": {
        "English":
            "Yellowing describes a visible loss of normal green coloration and may be associated with crop or nutritional conditions that need further assessment.",
        "Marathi":
            "पिवळेपणामध्ये पानांचा नैसर्गिक हिरवा रंग कमी होऊन पाने पिवळसर दिसू शकतात. कारण समजण्यासाठी पिकाची पुढील तपासणी आवश्यक आहे."
    }
}


# ============================================================
# ENGLISH PDF DATA
# ============================================================
# IMPORTANT:
# The WEBSITE follows the selected language.
# The PDF is ALWAYS generated in English.
# ============================================================

PDF_DISEASE_NAMES_ENGLISH = {
    "Healthy": "Healthy",
    "Mosaic": "Mosaic",
    "RedRot": "Red Rot",
    "Rust": "Rust",
    "Yellow": "Yellowing"
}

PDF_DISEASE_INFO_ENGLISH = {
    "Healthy": {
        "symptoms":
            "The leaf appears healthy without major visible disease symptoms.",
        "prevention":
            "Maintain proper irrigation, balanced nutrition, field sanitation and regular monitoring.",
        "recommendation":
            "Continue regular crop monitoring.",
        "management":
            "Maintain healthy crop practices and monitor the field regularly."
    },

    "Mosaic": {
        "symptoms":
            "Mosaic-like light and dark green patterns may appear on the leaf.",
        "prevention":
            "Use healthy planting material and regularly monitor the crop.",
        "recommendation":
            "Remove severely affected plants and follow local agricultural guidance.",
        "management":
            "Use healthy planting material and follow recommended disease-management practices."
    },

    "RedRot": {
        "symptoms":
            "Reddish or reddish-brown discoloration can occur in affected plant tissues.",
        "prevention":
            "Use healthy planting material and maintain good field sanitation.",
        "recommendation":
            "Inspect affected plants and consult an agricultural expert.",
        "management":
            "Remove severely affected plants where appropriate and follow recommended disease-management practices."
    },

    "Rust": {
        "symptoms":
            "Rust-colored spots or lesions may appear on the leaf surface.",
        "prevention":
            "Monitor the crop regularly and maintain proper crop management.",
        "recommendation":
            "Inspect affected leaves and follow recommended disease-management practices.",
        "management":
            "Monitor disease development and follow locally recommended crop-management practices."
    },

    "Yellow": {
        "symptoms":
            "The leaf may show yellowing or loss of normal green coloration.",
        "prevention":
            "Maintain balanced nutrition, irrigation and regular crop monitoring.",
        "recommendation":
            "Check crop nutrition and consult an agricultural expert if symptoms continue.",
        "management":
            "Check crop nutrition, irrigation and other field conditions before taking corrective action."
    }
}


# ============================================================
# PDF REPORT GENERATOR
# ============================================================

def create_disease_pdf(
    report_time,
    display_name,
    confidence_percentage,
    overview_text,
    info,
    is_marathi
):
    """Create a styled PDF matching the Streamlit website design."""

    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        SimpleDocTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle
    )

    # --------------------------------------------------------
    # FONT
    # --------------------------------------------------------

    font_candidates = [
        Path(r"C:\Windows\Fonts\Nirmala.ttf"),
        Path(r"C:\Windows\Fonts\NirmalaUI.ttf"),
        Path(r"C:\Windows\Fonts\mangal.ttf"),
        Path(r"C:\Windows\Fonts\NotoSansDevanagari-Regular.ttf"),
        Path(r"/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf"),
        Path(r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
    ]

    font_path = next((p for p in font_candidates if p.exists()), None)

    if font_path:
        if "SugarcanePDF" not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(
                TTFont("SugarcanePDF", str(font_path))
            )
        font_name = "SugarcanePDF"
    else:
        font_name = "Helvetica"

    # --------------------------------------------------------
    # COLORS - SAME STYLE AS STREAMLIT WEBSITE
    # --------------------------------------------------------

    DARK_GREEN = colors.HexColor("#14532D")
    FOOTER_GREEN = colors.HexColor("#123B27")
    LIGHT_GREEN = colors.HexColor("#F0FDF4")
    BORDER_GREEN = colors.HexColor("#BBF7D0")
    CARD_BORDER = colors.HexColor("#DDE7E0")
    TEXT = colors.HexColor("#475569")
    LIGHT_TEXT = colors.HexColor("#DCFCE7")
    WHITE = colors.white

    # --------------------------------------------------------
    # PAGE
    # --------------------------------------------------------

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=12 * mm,
        leftMargin=12 * mm,
        topMargin=10 * mm,
        bottomMargin=10 * mm,
        title="Sugarcane AI Disease Report",
        author="Sugarcane AI"
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "SugarcanePDFTitle",
        parent=styles["Title"],
        fontName=font_name,
        fontSize=20,
        leading=24,
        alignment=TA_CENTER,
        textColor=WHITE,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        "SugarcanePDFSubtitle",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=LIGHT_TEXT
    )

    card_title_style = ParagraphStyle(
        "SugarcanePDFCardTitle",
        parent=styles["Heading2"],
        fontName=font_name,
        fontSize=11.5,
        leading=14,
        textColor=DARK_GREEN,
        spaceAfter=5
    )

    card_body_style = ParagraphStyle(
        "SugarcanePDFCardBody",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=8.8,
        leading=12.5,
        textColor=TEXT
    )

    small_style = ParagraphStyle(
        "SugarcanePDFSmall",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=8,
        leading=11,
        textColor=TEXT
    )

    footer_style = ParagraphStyle(
        "SugarcanePDFFooter",
        parent=styles["BodyText"],
        fontName=font_name,
        fontSize=8,
        leading=11,
        alignment=TA_CENTER,
        textColor=LIGHT_TEXT
    )

    def paragraph(value, style=card_body_style):
        value = str(value)
        value = value.replace("&", "&amp;")
        value = value.replace("<", "&lt;")
        value = value.replace(">", "&gt;")
        value = value.replace("\n", "<br/>")
        return Paragraph(value, style)

    if is_marathi:
        title = "Sugarcane AI"
        subtitle = "AI-आधारित ऊस पान रोग निदान प्रणाली"
        date_label = "दिनांक"
        disease_label = "अंदाजित रोग"
        confidence_label = "विश्वास पातळी"
        overview_label = "रोगाची थोडक्यात माहिती"
        symptoms_label = "लक्षणे"
        prevention_label = "प्रतिबंध"
        recommendation_label = "शिफारस"
        management_label = "व्यवस्थापन"
        note = (
            "टीप: हा अहवाल मॉडेलच्या अंदाजावर आधारित आहे. "
            "कृषीविषयक निर्णयासाठी पात्र कृषी तज्ज्ञांचा सल्ला घ्या."
        )
    else:
        title = "Sugarcane AI"
        subtitle = "AI-Based Sugarcane Leaf Disease Detection System"
        date_label = "Date"
        disease_label = "Predicted Disease"
        confidence_label = "Confidence"
        overview_label = "Disease Overview"
        symptoms_label = "Symptoms"
        prevention_label = "Prevention"
        recommendation_label = "Recommendation"
        management_label = "Management"
        note = (
            "Note: This report is generated from the model prediction. "
            "Consult a qualified agricultural expert for agricultural decisions."
        )

    story = []

    # --------------------------------------------------------
    # GREEN WEBSITE-STYLE HEADER
    # --------------------------------------------------------

    header = Table([
        [Paragraph(title, title_style)],
        [Paragraph(subtitle, subtitle_style)]
    ], colWidths=[186 * mm])

    header.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), DARK_GREEN),
        ("TOPPADDING", (0, 0), (-1, 0), 13),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 2),
        ("TOPPADDING", (0, 1), (-1, 1), 1),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 13),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
    ]))

    story.append(header)
    story.append(Spacer(1, 8))

    # --------------------------------------------------------
    # DATE
    # --------------------------------------------------------

    date_box = Table([
        [paragraph(f"{date_label}: {report_time}", small_style)]
    ], colWidths=[186 * mm])

    date_box.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("BOX", (0, 0), (-1, -1), 0.7, CARD_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 9),
        ("RIGHTPADDING", (0, 0), (-1, -1), 9),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ]))

    story.append(date_box)
    story.append(Spacer(1, 8))

    # --------------------------------------------------------
    # RESULT SUMMARY - TWO COLUMNS
    # --------------------------------------------------------

    disease_value_style = ParagraphStyle(
        "DiseaseValue",
        parent=card_title_style,
        fontSize=15,
        leading=18
    )

    confidence_value_style = ParagraphStyle(
        "ConfidenceValue",
        parent=card_title_style,
        fontSize=15,
        leading=18,
        textColor=colors.HexColor("#16A34A")
    )

    disease_card = Table([
        [paragraph(disease_label, small_style)],
        [paragraph(display_name, disease_value_style)]
    ], colWidths=[89 * mm])

    disease_card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), WHITE),
        ("BOX", (0, 0), (-1, -1), 0.8, CARD_BORDER),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    confidence_card = Table([
        [paragraph(confidence_label, small_style)],
        [paragraph(f"{confidence_percentage:.2f}%", confidence_value_style)]
    ], colWidths=[89 * mm])

    confidence_card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.8, BORDER_GREEN),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ]))

    summary = Table(
        [[disease_card, confidence_card]],
        colWidths=[91 * mm, 91 * mm]
    )

    summary.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    story.append(summary)
    story.append(Spacer(1, 9))

    # --------------------------------------------------------
    # DISEASE OVERVIEW - LIGHT GREEN WEBSITE CARD
    # --------------------------------------------------------

    overview_card = Table([
        [
            paragraph(overview_label, card_title_style),
            paragraph(overview_text, card_body_style)
        ]
    ], colWidths=[50 * mm, 132 * mm])

    overview_card.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), LIGHT_GREEN),
        ("BOX", (0, 0), (-1, -1), 0.8, BORDER_GREEN),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))

    story.append(overview_card)
    story.append(Spacer(1, 9))

    # --------------------------------------------------------
    # 2 × 2 INFORMATION GRID - SAME AS WEBSITE
    # --------------------------------------------------------

    sections = [
        (symptoms_label, info["symptoms"]),
        (prevention_label, info["prevention"]),
        (recommendation_label, info["recommendation"]),
        (management_label, info["management"])
    ]

    cards = []

    for heading, content in sections:
        card = Table([
            [paragraph(heading, card_title_style)],
            [paragraph(content, card_body_style)]
        ], colWidths=[89 * mm], rowHeights=[None, None])

        card.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, -1), WHITE),
            ("BOX", (0, 0), (-1, -1), 0.8, CARD_BORDER),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 9),
            ("RIGHTPADDING", (0, 0), (-1, -1), 9),
            ("TOPPADDING", (0, 0), (-1, -1), 8),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
        ]))

        cards.append(card)

    information_grid = Table(
        [[cards[0], cards[1]], [cards[2], cards[3]]],
        colWidths=[91 * mm, 91 * mm]
    )

    information_grid.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
    ]))

    story.append(information_grid)
    story.append(Spacer(1, 9))

    # --------------------------------------------------------
    # FOOTER - SAME DARK GREEN STYLE
    # --------------------------------------------------------

    footer = Table([
        [Paragraph("Sugarcane AI Disease Detection", footer_style)],
        [Paragraph("AI-Based Research Project", footer_style)]
    ], colWidths=[186 * mm])

    footer.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), FOOTER_GREEN),
        ("LINEABOVE", (0, 0), (-1, 0), 2, colors.HexColor("#22C55E")),
        ("TOPPADDING", (0, 0), (-1, 0), 7),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 1),
        ("TOPPADDING", (0, 1), (-1, 1), 1),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 7),
    ]))

    story.append(footer)
    story.append(Spacer(1, 5))
    story.append(paragraph(note, small_style))

    document.build(story)

    return buffer.getvalue()


# ============================================================
# IMAGE QUALITY VALIDATION
# ============================================================

def validate_image_quality(image):
    """Basic image-quality check before model inference."""
    try:
        width, height = image.size

        if width < 120 or height < 120:
            return False

        brightness = ImageStat.Stat(
            image.convert("L")
        ).mean[0]

        if brightness < 12 or brightness > 245:
            return False

        return True

    except Exception:
        return False


# ============================================================
# DISEASE NAMES
# ============================================================


# ============================================================
# CUSTOM NAVIGATION BAR
# ============================================================

# Read the selected language from the URL.
# English = ?lang=en
# Marathi  = ?lang=mr
language = st.query_params.get("lang", "en")

if language not in ("en", "mr"):
    language = "en"

is_marathi = language == "mr"

with st.container():

    # MOBILE
    st.html(f"""
    <div class="custom-navbar">

        <div class="mobile-navbar">

            <div class="nav-logo">
                🌿 Sugarcane AI
            </div>

            <details class="mobile-menu">

                <summary aria-label="Open navigation menu">
                    ☰
                </summary>

                <div class="mobile-menu-content">

                    <a class="nav-link" href="?lang={language}">
                        🏠 {"मुख्यपृष्ठ" if is_marathi else "Home"}
                    </a>

                    <a class="nav-link" href="?page=about&lang={language}">
                        ℹ️ {"माहिती" if is_marathi else "About Us"}
                    </a>

                    <a class="nav-link" href="?page=how_it_works&lang={language}">
                        🔬 {"कार्यपद्धती" if is_marathi else "How It Works"}
                    </a>

                    <div class="mobile-language-title">
                        🌐 {"भाषा" if is_marathi else "Language"}
                    </div>

                    <div class="mobile-language-options">

                        <a href="?lang=en">
                            English
                        </a>

                        <a href="?lang=mr">
                            मराठी
                        </a>

                    </div>

                </div>

            </details>

        </div>


        <!-- DESKTOP -->

        <div class="desktop-navbar"
             style="
                width:100%;
                display:flex;
                align-items:center;
                justify-content:space-between;
             ">

            <div class="nav-logo">
                🌿 Sugarcane AI
            </div>

            <div class="desktop-nav">

                <a class="nav-link" href="?lang={language}">
                    {"मुख्यपृष्ठ" if is_marathi else "Home"}
                </a>

                <a class="nav-link" href="?page=about&lang={language}">
                    {"माहिती" if is_marathi else "About Us"}
                </a>

                <a class="nav-link" href="?page=how_it_works&lang={language}">
                    {"कार्यपद्धती" if is_marathi else "How It Works"}
                </a>

            </div>

            <div class="desktop-language">

                <details class="language-menu">

                    <summary>
                        {"मराठी" if is_marathi else "English"} ▾
                    </summary>

                    <div class="language-options">

                        <a href="?lang=en">
                            English
                        </a>

                        <a href="?lang=mr">
                            मराठी
                        </a>

                    </div>

                </details>

            </div>

        </div>

    </div>
    """)


# ============================================================
# SELECT LANGUAGE TEXT
# ============================================================

text = marathi if is_marathi else english


# ============================================================
# PROJECT HEADER
# ============================================================

st.html(f"""
<div class="project-header">

    <div class="header-title">
        {text["title"]}
    </div>

    <div class="header-subtitle">
        {text["subtitle"]}
    </div>

</div>
""")


# ============================================================
# TWO COLUMNS
# ============================================================

left, right = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# LEFT SIDE
# ============================================================

with left:

    st.html(f"""
    <div class="main-panel">

        <div class="panel-title">
            {text["upload_title"]}
        </div>

        <div class="panel-subtitle">
            {text["upload_subtitle"]}
        </div>

    </div>
    """)


    uploaded_file = st.file_uploader(
        text["choose_image"],
        type=[
            "jpg",
            "jpeg",
            "png"
        ],
        label_visibility="visible",
        key="leaf_image_uploader"
    )


    predict_clicked = False

    image = None


    if uploaded_file is not None:

        try:

            image = Image.open(
                uploaded_file
            ).convert("RGB")


            st.image(
                image,
                caption=text["uploaded_caption"],
                width=250
            )


            st.html(f"""
            <div class="upload-info">

                <b>{text["upload_success"]}</b>

                <br>

                {text["upload_ready"]}

            </div>
            """)


            predict_clicked = st.button(
                text["predict"],
                use_container_width=True,
                key="predict_button"
            )


        except Exception:

            st.error(
                text["invalid_image"]
            )

            image = None


    else:

        st.html(f"""
        <div class="upload-info">

            <b>{text["supported_formats"]}</b>

            <br>

            JPG, JPEG and PNG

            <br><br>

            <b>{text["tip"]}</b>

            <br>

            {text["tip_text"]}

        </div>
        """)


# ============================================================
# RIGHT SIDE
# ============================================================

with right:

    st.html(f"""
    <div class="main-panel">

        <div class="panel-title">
            {text["result_title"]}
        </div>

        <div class="panel-subtitle">
            {text["result_subtitle"]}
        </div>

    </div>
    """)


    if image is None:

        st.html(f"""
        <div class="waiting">

            <div class="waiting-icon">
                🌱
            </div>

            <div class="waiting-title">
                {text["waiting_title"]}
            </div>

            <div class="waiting-text">
                {text["waiting_text"]}
            </div>

        </div>
        """)


    elif not predict_clicked:

        st.html(f"""
        <div class="waiting">

            <div class="waiting-icon">
                🔎
            </div>

            <div class="waiting-title">
                {text["ready_title"]}
            </div>

            <div class="waiting-text">
                {text["ready_text"]}
            </div>

        </div>
        """)


    else:

        try:

            # ==================================================
            # IMAGE QUALITY CHECK
            # ==================================================

            if not validate_image_quality(image):

                st.warning(
                    text["invalid_image"]
                )

                st.stop()


            with st.spinner(
                text["analyzing"]
            ):

                results = model.predict(
                    source=image,
                    imgsz=224,
                    device="cpu",
                    verbose=False
                )


            result = results[0]


            top_index = int(    
                result.probs.top1
            )


            confidence = float(
                result.probs.top1conf
            )


            class_name = result.names[
                top_index
            ]


            confidence_percentage = (
                confidence * 100
            )


            disease_names = {

                "Healthy": "निरोगी पान",

                "Mosaic": "मोज़ेक रोग",

                "RedRot": "लाल कुज रोग",

                "Rust": "तांबेरा रोग",

                "Yellow": "पिवळेपणा"
            }


            display_name = (
                disease_names.get(
                    class_name,
                    class_name
                )
                if is_marathi
                else class_name
            )


            # ====================================================
            # PREDICTED DISEASE + CONFIDENCE
            # ====================================================

            st.html(f"""

            <div class="prediction-summary">

                <div class="summary-item">

                    <div class="summary-label">
                        {text["predicted_disease"]}
                    </div>

                    <div class="summary-value">
                        🌿 {display_name}
                    </div>

                </div>


                <div class="summary-item">

                    <div class="summary-label">
                        🎯 {text["confidence"]}
                    </div>

                    <div class="summary-value">
                        {confidence_percentage:.2f}%
                    </div>

                </div>

            </div>

            """)


            # ====================================================
            # CONFIDENCE BAR
            # ====================================================

            st.html(f"""

            <div class="confidence-bar">

                <div
                    class="confidence-fill"
                    style="width:{confidence_percentage}%"
                ></div>

            </div>

            """)


            # ====================================================
            # CONFIDENCE STATUS
            # ====================================================

            if confidence_percentage >= 80:
                confidence_status = text["confidence_high"]
            elif confidence_percentage >= 60:
                confidence_status = text["confidence_medium"]
            else:
                confidence_status = text["confidence_low"]

            st.html(f"""
            <div class="confidence-status">
                {confidence_status}
            </div>
            """)

            if confidence_percentage < 60:

                st.html(f"""
                <div class="low-confidence-card">
                    <b>{text["confidence_low"]}</b>
                    <br><br>
                    {text["low_confidence_message"]}
                </div>
                """)


            # ====================================================
            # PROBABILITY HEADING
            # ====================================================

            st.html(f"""
            <div class="probability-heading">
                {text["probability_title"]}
            </div>

            <div class="probability-subheading">
                {text["probability_subtitle"]}
            </div>
            """)


            probabilities = (
                result.probs.data
                .detach()
                .cpu()
                .tolist()
            )


            colors = {

                "Healthy": "#16A34A",

                "Mosaic": "#7C3AED",

                "RedRot": "#DC2626",

                "Rust": "#EA580C",

                "Yellow": "#CA8A04"

            }


            icons = {

                "Healthy": "🌿",

                "Mosaic": "🟣",

                "RedRot": "🔴",

                "Rust": "🟠",

                "Yellow": "🟡"

            }


            cards = ""


            for index, probability in enumerate(
                probabilities
            ):

                name = result.names[
                    index
                ]


                percentage = (
                    float(probability) * 100
                )


                color = colors.get(
                    name,
                    "#15803D"
                )


                icon = icons.get(
                    name,
                    "🌱"
                )


                display_probability_name = (

                    disease_names.get(
                        name,
                        name
                    )
                    if is_marathi
                    else name
                )


                if percentage >= 50:

                    status = text[
                        "most_likely"
                    ]

                elif percentage >= 5:

                    status = text[
                        "possible"
                    ]

                else:

                    status = text[
                        "low_probability"
                    ]


                cards += f"""

                <div class="probability-card">

                    <div class="probability-card-top">

                        <div class="probability-name">

                            <span class="probability-icon">
                                {icon}
                            </span>

                            <span>
                                {display_probability_name}
                            </span>

                        </div>


                        <div
                            class="probability-value"
                            style="color:{color};"
                        >
                            {percentage:.2f}%
                        </div>

                    </div>


                    <div class="probability-track">

                        <div
                            class="probability-fill"
                            style="
                                width:{percentage}%;
                                background:{color};
                            "
                        ></div>

                    </div>


                    <div class="probability-status">
                        {status}
                    </div>

                </div>

                """


            st.html(f"""

            <div class="probability-grid">

                {cards}

            </div>

            """)


            # ====================================================
            # DISEASE INFORMATION
            # ====================================================

            if is_marathi:

                disease_info = {

                    "Healthy": {

                        "symptoms":
                            "पानावर कोणत्याही मोठ्या रोगाची लक्षणे दिसत नाहीत. पानाचा रंग आणि रचना सामान्य दिसते.",

                        "prevention":
                            "योग्य सिंचन, संतुलित खत व्यवस्थापन आणि शेताची स्वच्छता राखा. पिकाची नियमित तपासणी करा.",

                        "recommendation":
                            "पिकाची नियमित पाहणी सुरू ठेवा आणि योग्य शेती व्यवस्थापन करा.",

                        "management":
                            "निरोगी लागवड साहित्य वापरा आणि पिकाची नियमित निगराणी ठेवा."
                    },

                    "Mosaic": {

                        "symptoms":
                            "कोवळ्या पानांवर फिकट आणि गडद हिरव्या रंगाचे पट्टे किंवा ठिपके दिसू शकतात. पानावर मोझेकसारखा रंगाचा नमुना तयार होतो.",

                        "prevention":
                            "निरोगी लागवड साहित्य वापरा आणि पिकाची नियमित तपासणी करा.",

                        "recommendation":
                            "रोगाची लक्षणे असलेली झाडे ओळखून त्यांचे योग्य व्यवस्थापन करा. आवश्यक असल्यास कृषी तज्ज्ञांचा सल्ला घ्या.",

                        "management":
                            "निरोगी लागवड साहित्य वापरा आणि रोगाचा प्रसार कमी करण्यासाठी रोगग्रस्त झाडांचे योग्य व्यवस्थापन करा."
                    },

                    "RedRot": {

                        "symptoms":
                            "रोगग्रस्त भागात लालसर किंवा लाल-तपकिरी रंगाचे बदल दिसू शकतात. कुजण्याची लक्षणे देखील दिसू शकतात.",

                        "prevention":
                            "निरोगी बेणे वापरा. शेताची स्वच्छता राखा आणि रोगग्रस्त वनस्पतींचे अवशेष शेतात ठेवू नका.",

                        "recommendation":
                            "रोगग्रस्त झाडांची तपासणी करा आणि योग्य रोग व्यवस्थापनासाठी कृषी तज्ज्ञांचा सल्ला घ्या.",

                        "management":
                            "गंभीरपणे रोगग्रस्त झाडांचे योग्य व्यवस्थापन करा आणि निरोगी लागवड साहित्याचा वापर करा."
                    },

                    "Rust": {

                        "symptoms":
                            "पानाच्या पृष्ठभागावर तांबूस-तपकिरी रंगाचे ठिपके किंवा डाग दिसू शकतात.",

                        "prevention":
                            "पिकाची नियमित तपासणी करा आणि शेतातील योग्य व्यवस्थापन ठेवा.",

                        "recommendation":
                            "रोगग्रस्त पाने तपासा आणि रोग वाढत असल्यास कृषी तज्ज्ञांचा सल्ला घ्या.",

                        "management":
                            "रोगाचा प्रसार नियमितपणे तपासा आणि स्थानिक कृषी मार्गदर्शक सूचनांनुसार योग्य व्यवस्थापन करा."
                    },

                    "Yellow": {

                        "symptoms":
                            "पानांचा हिरवा रंग कमी होऊन पाने पिवळसर दिसू शकतात. पानांचा नैसर्गिक हिरवा रंग फिका होतो.",

                        "prevention":
                            "संतुलित पोषण, योग्य सिंचन आणि नियमित पिक तपासणी करा.",

                        "recommendation":
                            "मातीतील पोषक घटक आणि सिंचनाची स्थिती तपासा. लक्षणे कायम राहिल्यास कृषी तज्ज्ञांचा सल्ला घ्या.",

                        "management":
                            "पिकाचे पोषण, सिंचन आणि शेतातील इतर परिस्थिती तपासा आणि आवश्यकतेनुसार योग्य उपाययोजना करा."
                    }
                }

            else:

                disease_info = {

                    "Healthy": {

                        "symptoms":
                            "The leaf appears healthy without major visible disease symptoms.",

                        "prevention":
                            "Maintain proper irrigation, balanced nutrition, field sanitation and regular monitoring.",

                        "recommendation":
                            "Continue regular crop monitoring.",

                        "management":
                            "Maintain healthy crop practices and monitor the field regularly."
                    },

                    "Mosaic": {

                        "symptoms":
                            "Mosaic-like light and dark green patterns may appear on the leaf.",

                        "prevention":
                            "Use healthy planting material and regularly monitor the crop.",

                        "recommendation":
                            "Remove severely affected plants and follow local agricultural guidance.",

                        "management":
                            "Use healthy planting material and follow recommended disease-management practices."
                    },

                    "RedRot": {

                        "symptoms":
                            "Reddish or reddish-brown discoloration can occur in affected plant tissues.",

                        "prevention":
                            "Use healthy planting material and maintain good field sanitation.",

                        "recommendation":
                            "Inspect affected plants and consult an agricultural expert.",

                        "management":
                            "Remove severely affected plants where appropriate and follow recommended disease-management practices."
                    },

                    "Rust": {

                        "symptoms":
                            "Rust-colored spots or lesions may appear on the leaf surface.",

                        "prevention":
                            "Monitor the crop regularly and maintain proper crop management.",

                        "recommendation":
                            "Inspect affected leaves and follow recommended disease-management practices.",

                        "management":
                            "Monitor disease development and follow locally recommended crop-management practices."
                    },

                    "Yellow": {

                        "symptoms":
                            "The leaf may show yellowing or loss of normal green coloration.",

                        "prevention":
                            "Maintain balanced nutrition, irrigation and regular crop monitoring.",

                        "recommendation":
                            "Check crop nutrition and consult an agricultural expert if symptoms continue.",

                        "management":
                            "Check crop nutrition, irrigation and other field conditions before taking corrective action."
                    }
                }


            info = disease_info.get(

                class_name,

                {

                    "symptoms":
                        "माहिती उपलब्ध नाही."
                        if is_marathi
                        else "Information is not available.",

                    "prevention":
                        "पिकाची नियमित तपासणी करा."
                        if is_marathi
                        else "Follow standard crop monitoring practices.",

                    "recommendation":
                        "कृषी तज्ज्ञांचा सल्ला घ्या."
                        if is_marathi
                        else "Consult an agricultural expert.",

                    "management":
                        "योग्य कृषी व्यवस्थापन पद्धती वापरा."
                        if is_marathi
                        else "Follow appropriate agricultural management practices."
                }

            )


            # ====================================================
            # INFORMATION HEADING
            # ====================================================

            st.html(f"""

            <div class="information-heading">
                {text["information_title"]}
            </div>

            <div class="information-subheading">
                {text["information_subtitle"]}
            </div>

            """)


            # ====================================================
            # 2 x 2 INFORMATION GRID
            # ====================================================

            st.html(f"""

            <div class="info-grid">


                <div class="info">

                    <div class="info-title">
                        {text["symptoms"]}
                    </div>

                    <div class="info-text">
                        {info["symptoms"]}
                    </div>

                </div>


                <div class="info">

                    <div class="info-title">
                        {text["prevention"]}
                    </div>

                    <div class="info-text">
                        {info["prevention"]}
                    </div>

                </div>


                <div class="info">

                    <div class="info-title">
                        {text["recommendation"]}
                    </div>

                    <div class="info-text">
                        {info["recommendation"]}
                    </div>

                </div>


                <div class="info">

                    <div class="info-title">
                        {text["management"]}
                    </div>

                    <div class="info-text">
                        {info["management"]}
                    </div>

                </div>


            </div>

            """)


            # ====================================================
            # DISEASE OVERVIEW
            # ====================================================

            overview_language = "Marathi" if is_marathi else "English"

            overview_text = overview_info.get(
                class_name,
                {}
            ).get(
                overview_language,
                "माहिती उपलब्ध नाही."
                if is_marathi
                else "Information is not available."
            )

            st.html(f"""
            <div class="overview-card">
                <div class="overview-title">
                    {text["overview_title"]}
                </div>
                <div class="overview-text">
                    {overview_text}
                </div>
            </div>
            """)


            # ====================================================
            # DOWNLOAD DISEASE REPORT - PDF
            # ====================================================

            report_time = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            # ====================================================
            # PDF DATA IS ALWAYS ENGLISH
            # ====================================================
            # The webpage continues using the selected language.
            # Only the PDF uses these English values.

            pdf_display_name = PDF_DISEASE_NAMES_ENGLISH.get(
                class_name,
                class_name
            )

            pdf_overview_text = overview_info.get(
                class_name,
                {}
            ).get(
                "English",
                "Information is not available."
            )

            pdf_info = PDF_DISEASE_INFO_ENGLISH.get(
                class_name,
                {
                    "symptoms": "Information is not available.",
                    "prevention": "Follow standard crop monitoring practices.",
                    "recommendation": "Consult an agricultural expert.",
                    "management": "Follow appropriate agricultural management practices."
                }
            )

            pdf_bytes = create_disease_pdf(
                report_time=report_time,
                display_name=pdf_display_name,
                confidence_percentage=confidence_percentage,
                overview_text=pdf_overview_text,
                info=pdf_info,
                is_marathi=False
            )

            st.html(f"""
            <div class="report-box">
                <div class="report-title">
                    {text["download_title"]}
                </div>
            </div>
            """)

            st.download_button(
                label=text["download_report"],
                data=pdf_bytes,
                file_name="sugarcane_disease_report.pdf",
                mime="application/pdf",
                use_container_width=True,
                key="download_disease_report_pdf"
            )


        except Exception as e:

            st.error(
                text["prediction_failed"]
            )

            st.exception(e)


# ============================================================
# FOOTER
# ============================================================

st.html(f"""

<div class="project-footer">

    {text["footer"]}

</div>

""")    