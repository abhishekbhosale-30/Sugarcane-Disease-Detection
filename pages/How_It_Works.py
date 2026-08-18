import streamlit as st

st.set_page_config(
    page_title="How It Works | Sugarcane AI",
    page_icon="🔬",
    layout="wide"
)

# ============================================================
# PAGE NAVIGATION
# ============================================================

requested_page = st.query_params.get("page")

if requested_page == "about":
    st.switch_page("pages/About_Us.py")

elif requested_page == "home":
    st.switch_page("app.py")


# ============================================================
# LANGUAGE
# ============================================================

language = st.query_params.get("lang", "en")

if language not in ["en", "mr"]:
    language = "en"

is_marathi = language == "mr"


# ============================================================
# ENGLISH CONTENT
# ============================================================

english = {

    "home": "Home",
    "about": "About Us",
    "how": "How It Works",
    "language": "Language",

    "header_title": "🔬 How It Works",
    "header_subtitle":
        "Sugarcane AI Disease Detection Process",

    "step1_title": "📤 Upload Image",
    "step1_text":
        "Upload a clear sugarcane leaf image using "
        "the image upload option.",

    "step2_title": "🤖 AI Analysis",
    "step2_text":
        "The uploaded sugarcane leaf image is analyzed "
        "by the trained AI classification model.",

    "step3_title": "📊 Disease Prediction",
    "step3_text":
        "The system calculates the probability of the "
        "trained disease classes and identifies the "
        "most probable disease.",

    "step4_title": "🌿 Result",
    "step4_text":
        "The system displays the predicted disease, "
        "confidence and useful disease-management "
        "information.",

    "flow_title": "🔄 Detection Process",

    "flow1": "📷 Sugarcane Leaf Image",
    "flow2": "🧠 AI Model",
    "flow3": "📊 Prediction",
    "flow4": "🌿 Disease Result",

    "ai_title": "🧠 AI Model",
    "ai_text":
        "Sugarcane AI uses a trained image-classification "
        "model to analyze sugarcane leaf images and "
        "identify the most probable disease class.",

    "confidence_title": "🎯 Confidence",
    "confidence_text":
        "The confidence percentage represents how strongly "
        "the model supports the predicted disease. "
        "The disease with the highest probability is "
        "selected as the prediction.",

    "probability_title": "📈 Probability Analysis",
    "probability_text":
        "The application can display the probability "
        "distribution of the different trained disease "
        "classes to help understand the model prediction.",

    "disease_title": "🌱 Disease Information",
    "disease_text":
        "After prediction, the application provides "
        "useful information such as symptoms, prevention, "
        "recommendations and management.",

    "footer":
        "🌿 Sugarcane AI Disease Detection | "
        "AI-Based Research Project"
}


# ============================================================
# MARATHI CONTENT
# ============================================================

marathi = {

    "home": "मुख्यपृष्ठ",
    "about": "आमच्याबद्दल",
    "how": "कार्यपद्धती",
    "language": "भाषा",

    "header_title": "🔬 हे कसे कार्य करते",
    "header_subtitle":
        "Sugarcane AI रोग ओळख प्रक्रिया",

    "step1_title": "📤 प्रतिमा अपलोड करा",
    "step1_text":
        "प्रतिमा अपलोड करण्याच्या पर्यायाचा वापर करून "
        "ऊसाच्या पानाची स्पष्ट प्रतिमा अपलोड करा.",

    "step2_title": "🤖 AI विश्लेषण",
    "step2_text":
        "अपलोड केलेल्या ऊसाच्या पानाच्या प्रतिमेचे "
        "प्रशिक्षित AI वर्गीकरण मॉडेलद्वारे विश्लेषण केले जाते.",

    "step3_title": "📊 रोगाचा अंदाज",
    "step3_text":
        "प्रणाली प्रशिक्षित रोग वर्गांची संभाव्यता मोजते "
        "आणि सर्वाधिक संभाव्यता असलेला रोग ओळखते.",

    "step4_title": "🌿 निकाल",
    "step4_text":
        "प्रणाली अंदाजित रोग, विश्वास पातळी आणि "
        "रोग व्यवस्थापनाशी संबंधित उपयुक्त माहिती दर्शवते.",

    "flow_title": "🔄 रोग ओळख प्रक्रिया",

    "flow1": "📷 ऊसाच्या पानाची प्रतिमा",
    "flow2": "🧠 AI मॉडेल",
    "flow3": "📊 अंदाज",
    "flow4": "🌿 रोगाचा निकाल",

    "ai_title": "🧠 AI मॉडेल",
    "ai_text":
        "Sugarcane AI प्रशिक्षित प्रतिमा-वर्गीकरण मॉडेलचा "
        "वापर करून ऊसाच्या पानांच्या प्रतिमांचे विश्लेषण "
        "करते आणि संभाव्य रोग वर्ग ओळखते.",

    "confidence_title": "🎯 विश्वास पातळी",
    "confidence_text":
        "विश्वासाची टक्केवारी मॉडेलला अंदाजित रोगाबद्दल "
        "किती विश्वास आहे हे दर्शवते. सर्वाधिक संभाव्यता "
        "असलेला रोग अंदाज म्हणून निवडला जातो.",

    "probability_title": "📈 संभाव्यता विश्लेषण",
    "probability_text":
        "मॉडेलच्या अंदाजाचे विश्लेषण समजण्यासाठी प्रणाली "
        "विविध प्रशिक्षित रोग वर्गांचे संभाव्यता वितरण "
        "दर्शवू शकते.",

    "disease_title": "🌱 रोगाची माहिती",
    "disease_text":
        "रोगाचा अंदाज आल्यानंतर प्रणाली लक्षणे, प्रतिबंध, "
        "शिफारस आणि व्यवस्थापन यासारखी उपयुक्त माहिती देते.",

    "footer":
        "🌿 Sugarcane AI रोग ओळख प्रणाली | "
        "कृत्रिम बुद्धिमत्तेवर आधारित संशोधन प्रकल्प"
}

text = marathi if is_marathi else english


# ============================================================
# CSS
# ============================================================

st.html("""
<style>

/* ============================================================
   GENERAL
   ============================================================ */

.stApp {
    background: #F3F7F4;
}

.block-container {
    max-width: 1250px;
    padding-top: 30px;
    padding-bottom: 80px;
}


/* ============================================================
   NAVBAR
   ============================================================ */

.how-navbar {

    width: 100%;
    margin-top: 50px;
    min-height: 64px;

    background: #14532D;

    border-radius: 0px 35px;

    padding: 0 22px;

    box-sizing: border-box;

    display: flex;

    align-items: center;

    justify-content: space-between;

    position: relative;

    z-index: 9999;

    box-shadow:
        0 5px 18px rgba(20, 83, 45, 0.12);
}


/* LOGO */

.how-navbar-logo {

    color: #FFFFFF;

    font-size: 17px;

    font-weight: 800;

    white-space: nowrap;
}


/* ============================================================
   DESKTOP NAVIGATION
   ============================================================ */

.how-desktop-nav {

    display: flex;

    align-items: center;

    justify-content: flex-end;

    gap: 28px;
}


.how-nav-link {

    color: #DCFCE7 !important;

    text-decoration: none !important;

    font-size: 13px;

    font-weight: 600;

    white-space: nowrap;

    padding: 8px 4px;

    transition: 0.2s ease;
}


.how-nav-link:hover {

    color: #FFFFFF !important;
}


/* ============================================================
   DESKTOP LANGUAGE
   ============================================================ */

.how-language {

    position: relative;
}


.how-language summary {

    color: #DCFCE7;

    font-size: 13px;

    font-weight: 600;

    cursor: pointer;

    list-style: none;

    white-space: nowrap;
}


.how-language summary::-webkit-details-marker {

    display: none;
}


.how-language-menu {

    position: absolute;

    right: 0;

    top: 32px;

    width: 125px;

    background: #14532D;

    border-radius: 9px;

    padding: 6px;

    box-shadow:
        0 8px 20px rgba(0, 0, 0, 0.20);
}


.how-language-menu a {

    display: block;

    color: #DCFCE7 !important;

    text-decoration: none !important;

    padding: 9px;

    font-size: 12px;

    font-weight: 600;

    border-radius: 6px;
}


.how-language-menu a:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* ============================================================
   MOBILE MENU
   ============================================================ */

.how-mobile-menu {

    display: none;

    position: relative;
}


.how-mobile-menu summary {

    display: flex;

    align-items: center;

    justify-content: center;

    width: 42px;

    height: 42px;

    color: #DCFCE7;

    font-size: 27px;

    font-weight: 800;

    cursor: pointer;

    list-style: none;
}


.how-mobile-menu summary::-webkit-details-marker {

    display: none;
}


/* MOBILE DROPDOWN */

.how-mobile-content {

    position: absolute;

    right: 0;

    top: 50px;

    width: 220px;

    background: #14532D;

    border-radius: 12px;

    padding: 8px;

    box-shadow:
        0 10px 25px rgba(0, 0, 0, 0.20);

    z-index: 10000;
}


.how-mobile-link {

    display: block;

    width: 100%;

    box-sizing: border-box;

    color: #DCFCE7 !important;

    text-decoration: none !important;

    padding: 12px;

    font-size: 13px;

    font-weight: 600;

    border-radius: 7px;
}


.how-mobile-link:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* MOBILE LANGUAGE */

.how-mobile-language-title {

    color: #DCFCE7;

    font-size: 11px;

    font-weight: 700;

    padding: 12px 12px 6px;
}


.how-mobile-language {

    display: flex;

    gap: 5px;

    padding: 0 5px 6px;
}


.how-mobile-language a {

    flex: 1;

    text-align: center;

    color: #DCFCE7 !important;

    text-decoration: none !important;

    font-size: 11px;

    font-weight: 700;

    padding: 8px;

    border-radius: 6px;

    background: transparent;
}


.how-mobile-language a:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* ============================================================
   HOW IT WORKS HEADER
   ============================================================ */

.how-header {

    background: #14532D;

    border-radius: 0px 50px;

    padding: 30px;

    margin-bottom: 25px;

    margin-top: 30px;

    box-shadow:
        0 5px 18px rgba(20, 83, 45, 0.12);
}


.how-title {

    color: #FFFFFF;

    font-size: 32px;

    font-weight: 800;

    margin-bottom: 8px;
}


.how-subtitle {

    color: #DCFCE7;

    font-size: 15px;
}


/* ============================================================
   STEP GRID
   ============================================================ */

.steps-grid {

    display: grid;

    grid-template-columns: repeat(4, 1fr);

    gap: 16px;

    margin-top: 20px;
}


.step-card {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 14px;

    padding: 22px;

    min-height: 190px;

    box-shadow:
        0 4px 14px rgba(20, 83, 45, 0.06);
}


.step-number {

    width: 38px;

    height: 38px;

    border-radius: 50%;

    background: #14532D;

    color: #FFFFFF;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 17px;

    font-weight: 800;

    margin-bottom: 14px;
}


.step-card h2 {

    color: #14532D;

    font-size: 18px;

    margin: 0 0 10px 0;
}


.step-card p {

    color: #475569;

    font-size: 13px;

    line-height: 1.6;

    margin: 0;
}


/* ============================================================
   FLOW
   ============================================================ */

.flow-section {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 14px;

    padding: 25px;

    margin-top: 22px;

    box-shadow:
        0 4px 14px rgba(20, 83, 45, 0.06);
}


.flow-title {

    color: #14532D;

    font-size: 22px;

    font-weight: 800;

    margin-bottom: 20px;
}


.flow {

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 10px;

    flex-wrap: wrap;
}


.flow-box {

    background: #F0FDF4;

    border: 1px solid #BBF7D0;

    border-radius: 10px;

    padding: 14px 18px;

    color: #14532D;

    font-weight: 700;

    text-align: center;
}


.arrow {

    color: #16A34A;

    font-size: 22px;

    font-weight: 800;
}


/* ============================================================
   INFORMATION
   ============================================================ */

.info-grid {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 18px;

    margin-top: 22px;
}


.info-card {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 14px;

    padding: 22px;

    box-shadow:
        0 4px 14px rgba(20, 83, 45, 0.06);
}


.info-card h2 {

    color: #14532D;

    font-size: 19px;

    margin: 0 0 10px 0;
}


.info-card p {

    color: #475569;

    font-size: 13px;

    line-height: 1.7;

    margin: 0;
}


/* ============================================================
   FOOTER
   ============================================================ */

.how-footer {

    margin-top: 30px;

    background: #123B27;

    color: #DCFCE7;

    text-align: center;

    padding: 12px;

    border-top: 2px solid #22C55E;

    border-radius: 8px;

    font-size: 12px;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {

        padding-left: 12px;

        padding-right: 12px;
    }


    /* NAVBAR MUST STAY ONE ROW */

    .how-navbar {

        min-height: 64px;

        padding: 0 16px;

        border-radius: 0px 35px;

        flex-direction: row;

        align-items: center;

        justify-content: space-between;
    }


    .how-navbar-logo {

        font-size: 16px;

        line-height: 1;

        display: flex;

        align-items: center;
    }


    /* HIDE DESKTOP NAVIGATION */

    .how-desktop-nav {

        display: none;
    }


    /* SHOW HAMBURGER */

    .how-mobile-menu {

        display: block;
    }


    /* HOW HEADER */

    .how-header {

        padding: 22px;

        border-radius: 0px 35px;
    }


    .how-title {

        font-size: 23px;
    }


    .how-subtitle {

        font-size: 12px;
    }


    /* STEP GRID */

    .steps-grid {

        grid-template-columns: 1fr 1fr;

        gap: 8px;
    }


    .step-card {

        padding: 12px;

        min-height: 160px;
    }


    .step-number {

        width: 30px;

        height: 30px;

        font-size: 13px;

        margin-bottom: 8px;
    }


    .step-card h2 {

        font-size: 13px;
    }


    .step-card p {

        font-size: 10px;

        line-height: 1.5;
    }


    /* FLOW */

    .flow-section {

        padding: 15px;
    }


    .flow-title {

        font-size: 18px;
    }


    .flow {

        flex-direction: column;
    }


    .flow-box {

        width: 100%;

        box-sizing: border-box;

        font-size: 11px;
    }


    .arrow {

        transform: rotate(90deg);
    }


    /* INFORMATION */

    .info-grid {

        grid-template-columns: 1fr 1fr;

        gap: 8px;
    }


    .info-card {

        padding: 12px;
    }


    .info-card h2 {

        font-size: 13px;
    }


    .info-card p {

        font-size: 10px;

        line-height: 1.5;
    }


    .how-footer {

        font-size: 9px;
    }

}

</style>
""")


# ============================================================
# NAVBAR
# ============================================================

st.html(f"""
<div class="how-navbar">

    <!-- LOGO -->

    <div class="how-navbar-logo">
        🌿 Sugarcane AI
    </div>


    <!-- DESKTOP NAVIGATION -->

    <div class="how-desktop-nav">

        <a
            class="how-nav-link"
            href="/?lang={language}"
        >
            🏠 {text["home"]}
        </a>


        <a
            class="how-nav-link"
            href="?page=about&lang={language}"
        >
            ℹ️ {text["about"]}
        </a>


        <a
            class="how-nav-link"
            href="?lang={language}"
        >
            🔬 {text["how"]}
        </a>


        <details class="how-language">

            <summary>
                🌐 {"मराठी" if is_marathi else "English"} ▾
            </summary>


            <div class="how-language-menu">

                <a href="?lang=en">
                    English
                </a>

                <a href="?lang=mr">
                    मराठी
                </a>

            </div>

        </details>

    </div>


    <!-- MOBILE HAMBURGER -->

    <details class="how-mobile-menu">

        <summary aria-label="Open navigation menu">
            ☰
        </summary>


        <div class="how-mobile-content">

            <a
                class="how-mobile-link"
                href="/?lang={language}"
            >
                🏠 {text["home"]}
            </a>


            <a
                class="how-mobile-link"
                href="?page=about&lang={language}"
            >
                ℹ️ {text["about"]}
            </a>


            <a
                class="how-mobile-link"
                href="?lang={language}"
            >
                🔬 {text["how"]}
            </a>


            <div class="how-mobile-language-title">

                🌐 {text["language"]}

            </div>


            <div class="how-mobile-language">

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
""")


# ============================================================
# HEADER
# ============================================================

st.html(f"""
<div class="how-header">

    <div class="how-title">
        {text["header_title"]}
    </div>

    <div class="how-subtitle">
        {text["header_subtitle"]}
    </div>

</div>
""")


# ============================================================
# FOUR STEPS
# ============================================================

st.html(f"""
<div class="steps-grid">

    <div class="step-card">

        <div class="step-number">
            1
        </div>

        <h2>
            {text["step1_title"]}
        </h2>

        <p>
            {text["step1_text"]}
        </p>

    </div>


    <div class="step-card">

        <div class="step-number">
            2
        </div>

        <h2>
            {text["step2_title"]}
        </h2>

        <p>
            {text["step2_text"]}
        </p>

    </div>


    <div class="step-card">

        <div class="step-number">
            3
        </div>

        <h2>
            {text["step3_title"]}
        </h2>

        <p>
            {text["step3_text"]}
        </p>

    </div>


    <div class="step-card">

        <div class="step-number">
            4
        </div>

        <h2>
            {text["step4_title"]}
        </h2>

        <p>
            {text["step4_text"]}
        </p>

    </div>

</div>
""")


# ============================================================
# PROCESS FLOW
# ============================================================

st.html(f"""
<div class="flow-section">

    <div class="flow-title">
        {text["flow_title"]}
    </div>

    <div class="flow">

        <div class="flow-box">
            {text["flow1"]}
        </div>

        <div class="arrow">
            →
        </div>

        <div class="flow-box">
            {text["flow2"]}
        </div>

        <div class="arrow">
            →
        </div>

        <div class="flow-box">
            {text["flow3"]}
        </div>

        <div class="arrow">
            →
        </div>

        <div class="flow-box">
            {text["flow4"]}
        </div>

    </div>

</div>
""")


# ============================================================
# INFORMATION CARDS
# ============================================================

st.html(f"""
<div class="info-grid">

    <div class="info-card">

        <h2>
            {text["ai_title"]}
        </h2>

        <p>
            {text["ai_text"]}
        </p>

    </div>


    <div class="info-card">

        <h2>
            {text["confidence_title"]}
        </h2>

        <p>
            {text["confidence_text"]}
        </p>

    </div>


    <div class="info-card">

        <h2>
            {text["probability_title"]}
        </h2>

        <p>
            {text["probability_text"]}
        </p>

    </div>


    <div class="info-card">

        <h2>
            {text["disease_title"]}
        </h2>

        <p>
            {text["disease_text"]}
        </p>

    </div>

</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html(f"""
<div class="how-footer">

    {text["footer"]}

</div>
""")