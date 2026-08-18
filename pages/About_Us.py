import streamlit as st

st.set_page_config(
    page_title="About Us | Sugarcane AI",
    page_icon="🌿",
    layout="wide"
)

# ============================================================
# LANGUAGE
# ============================================================

language = st.query_params.get("lang", "en")

if language not in ["en", "mr"]:
    language = "en"

is_marathi = language == "mr"


# ============================================================
# TRANSLATIONS
# ============================================================

english = {
    "home": "Home",
    "about": "About Us",
    "how": "How It Works",
    "language": "Language",

    "title": "🌿 Sugarcane AI",
    "subtitle": "AI-Based Sugarcane Leaf Disease Detection System",

    "project_title": "🌿 About the Project",
    "project_text": """
    Sugarcane AI is an AI-based research project designed
    to identify sugarcane leaf diseases from uploaded images.
    The system uses a trained YOLO classification model
    to analyze the image and provide a predicted disease
    along with its confidence score.
    """,

    "objective_title": "🎯 Our Objective",
    "objective_text": """
    The main objective of this project is to provide a simple
    and accessible method for detecting sugarcane leaf diseases.
    Early identification can help users understand the possible
    disease condition and take appropriate agricultural action.
    """,

    "technology_title": "🤖 AI Technology",
    "technology_text": """
    The application uses a YOLO classification model trained
    on sugarcane leaf disease classes. After an image is uploaded,
    the model calculates the probability of each trained class
    and displays the most likely prediction.
    """,

    "analysis_title": "📊 Prediction Analysis",
    "analysis_text": """
    The system displays the predicted disease, confidence score,
    probability distribution and additional information such as
    symptoms, prevention, recommendation and management.
    """,

    "footer": "🌿 Sugarcane AI Disease Detection | YOLO Classification Model | Research Project"
}


marathi = {
    "home": "मुख्यपृष्ठ",
    "about": "आमच्याबद्दल",
    "how": "कार्यपद्धती",
    "language": "भाषा",

    "title": "🌿 Sugarcane AI",
    "subtitle": "कृत्रिम बुद्धिमत्तेवर आधारित ऊस पान रोग ओळख प्रणाली",

    "project_title": "🌿 प्रकल्पाबद्दल",
    "project_text": """
    Sugarcane AI हा कृत्रिम बुद्धिमत्तेवर आधारित संशोधन प्रकल्प आहे,
    जो अपलोड केलेल्या प्रतिमेवरून ऊसाच्या पानांवरील रोग ओळखण्यासाठी
    तयार करण्यात आला आहे. ही प्रणाली प्रशिक्षित YOLO वर्गीकरण मॉडेलचा
    वापर करून प्रतिमेचे विश्लेषण करते आणि संभाव्य रोगासोबत त्याचा
    विश्वास स्तर दर्शवते.
    """,

    "objective_title": "🎯 आमचे उद्दिष्ट",
    "objective_text": """
    या प्रकल्पाचे मुख्य उद्दिष्ट ऊसाच्या पानांवरील रोग ओळखण्यासाठी
    सोपी आणि सहज उपलब्ध पद्धत उपलब्ध करून देणे आहे.
    रोगाची लवकर ओळख झाल्यास संभाव्य रोगस्थिती समजून घेण्यास
    आणि योग्य कृषी उपाययोजना करण्यास मदत होऊ शकते.
    """,

    "technology_title": "🤖 कृत्रिम बुद्धिमत्ता तंत्रज्ञान",
    "technology_text": """
    या प्रणालीमध्ये ऊसाच्या पानांवरील विविध रोगांच्या वर्गांवर
    प्रशिक्षित YOLO वर्गीकरण मॉडेलचा वापर केला आहे.
    प्रतिमा अपलोड केल्यानंतर मॉडेल प्रत्येक प्रशिक्षित वर्गाची
    संभाव्यता मोजते आणि सर्वाधिक संभाव्यता असलेला रोग दर्शवते.
    """,

    "analysis_title": "📊 अंदाजाचे विश्लेषण",
    "analysis_text": """
    प्रणाली अंदाजित रोग, विश्वास पातळी, संभाव्यता वितरण तसेच
    लक्षणे, प्रतिबंध, शिफारस आणि व्यवस्थापन यांसारखी
    अतिरिक्त माहिती प्रदर्शित करते.
    """,

    "footer": "🌿 Sugarcane AI रोग ओळख प्रणाली | YOLO वर्गीकरण मॉडेल | संशोधन प्रकल्प"
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

.about-navbar {
    width: 100%;
    min-height: 64px;
    margin-top: 50px;
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

.about-navbar-logo {
    color: #FFFFFF;

    font-size: 17px;

    font-weight: 800;

    white-space: nowrap;
}


/* ============================================================
   DESKTOP NAVIGATION
   ============================================================ */

.about-desktop-nav {

    display: flex;

    align-items: center;

    justify-content: flex-end;

    gap: 28px;
}


.about-nav-link {

    color: #DCFCE7 !important;

    text-decoration: none !important;

    font-size: 13px;

    font-weight: 600;

    white-space: nowrap;

    padding: 8px 4px;

    transition: 0.2s ease;
}


.about-nav-link:hover {

    color: #FFFFFF !important;
}


/* ============================================================
   DESKTOP LANGUAGE
   ============================================================ */

.about-language {

    position: relative;
}


.about-language summary {

    color: #DCFCE7;

    font-size: 13px;

    font-weight: 600;

    cursor: pointer;

    list-style: none;

    white-space: nowrap;
}


.about-language summary::-webkit-details-marker {

    display: none;
}


.about-language-menu {

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


.about-language-menu a {

    display: block;

    color: #DCFCE7 !important;

    text-decoration: none !important;

    padding: 9px;

    font-size: 12px;

    font-weight: 600;

    border-radius: 6px;
}


.about-language-menu a:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* ============================================================
   MOBILE MENU
   ============================================================ */

.about-mobile-menu {

    display: none;

    position: relative;
}


.about-mobile-menu summary {

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


.about-mobile-menu summary::-webkit-details-marker {

    display: none;
}


/* MOBILE DROPDOWN */

.about-mobile-content {

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


.about-mobile-link {

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


.about-mobile-link:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* MOBILE LANGUAGE */

.about-mobile-language-title {

    color: #DCFCE7;

    font-size: 11px;

    font-weight: 700;

    padding: 12px 12px 6px;
}


.about-mobile-language {

    display: flex;

    gap: 5px;

    padding: 0 5px 6px;
}


.about-mobile-language a {

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


.about-mobile-language a:hover {

    background: #166534;

    color: #FFFFFF !important;
}


/* ============================================================
   ABOUT HEADER
   ============================================================ */

.about-header {

    background: #14532D;

    border-radius: 0px 50px;

    padding: 30px;

    margin-bottom: 25px;

    margin-top: 30px;

    box-shadow:
        0 5px 18px rgba(20, 83, 45, 0.12);
}


.about-title {

    color: #FFFFFF;

    font-size: 32px;

    font-weight: 800;

    margin-bottom: 8px;
}


.about-subtitle {

    color: #DCFCE7;

    font-size: 15px;
}


/* ============================================================
   CARDS
   ============================================================ */

.about-grid {

    display: grid;

    grid-template-columns: 1fr 1fr;

    gap: 18px;
}


.about-card {

    background: #FFFFFF;

    border: 1px solid #DDE7E0;

    border-radius: 14px;

    padding: 22px;

    box-shadow:
        0 4px 14px rgba(20, 83, 45, 0.06);
}


.about-card h2 {

    color: #14532D;

    font-size: 20px;

    margin-bottom: 10px;
}


.about-card p {

    color: #475569;

    font-size: 14px;

    line-height: 1.7;
}


/* ============================================================
   FOOTER
   ============================================================ */

.about-footer {

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


    /* Navbar stays in ONE ROW */

    .about-navbar {

        min-height: 64px;

        padding: 0 16px;

        border-radius: 0px 35px;

        flex-direction: row;

        align-items: center;

        justify-content: space-between;
    }


    .about-navbar-logo {

        font-size: 16px;

        line-height: 1;

        display: flex;

        align-items: center;
    }


    /* Hide desktop navigation */

    .about-desktop-nav {

        display: none;
    }


    /* Show hamburger */

    .about-mobile-menu {

        display: block;
    }


    /* About header */

    .about-header {

        padding: 22px;

        border-radius: 0px 35px;

        margin-top: 25px;
    }


    .about-title {

        font-size: 23px;
    }


    .about-subtitle {

        font-size: 12px;
    }


    /* Cards */

    .about-grid {

        grid-template-columns: 1fr 1fr;

        gap: 8px;
    }


    .about-card {

        padding: 12px;
    }


    .about-card h2 {

        font-size: 13px;
    }


    .about-card p {

        font-size: 10px;

        line-height: 1.5;
    }


    .about-footer {

        font-size: 9px;
    }

}

</style>
""")


# ============================================================
# NAVBAR
# ============================================================

st.html(f"""
<div class="about-navbar">

    <!-- LOGO -->

    <div class="about-navbar-logo">
        🌿 Sugarcane AI
    </div>


    <!-- DESKTOP NAVIGATION -->

    <div class="about-desktop-nav">

        <a
            class="about-nav-link"
            href="/?lang={language}"
        >
            🏠 {text["home"]}
        </a>


        <a
            class="about-nav-link"
            href="/About_Us?lang={language}"
        >
            ℹ️ {text["about"]}
        </a>


        <a
            class="about-nav-link"
            href="/How_It_Works?lang={language}"
        >
            🔬 {text["how"]}
        </a>


        <details class="about-language">

            <summary>
                🌐 {"मराठी" if is_marathi else "English"} ▾
            </summary>


            <div class="about-language-menu">

                <a href="/About_Us?lang=en">
                    English
                </a>

                <a href="/About_Us?lang=mr">
                    मराठी
                </a>

            </div>

        </details>

    </div>


    <!-- MOBILE HAMBURGER -->

    <details class="about-mobile-menu">

        <summary aria-label="Open navigation menu">
            ☰
        </summary>


        <div class="about-mobile-content">

            <a
                class="about-mobile-link"
                href="/?lang={language}"
            >
                🏠 {text["home"]}
            </a>


            <a
                class="about-mobile-link"
                href="/About_Us?lang={language}"
            >
                ℹ️ {text["about"]}
            </a>


            <a
                class="about-mobile-link"
                href="/How_It_Works?lang={language}"
            >
                🔬 {text["how"]}
            </a>


            <div class="about-mobile-language-title">

                🌐 {text["language"]}

            </div>


            <div class="about-mobile-language">

                <a href="/About_Us?lang=en">
                    English
                </a>


                <a href="/About_Us?lang=mr">
                    मराठी
                </a>

            </div>

        </div>

    </details>

</div>
""")


# ============================================================
# ABOUT HEADER
# ============================================================

st.html(f"""
<div class="about-header">

    <div class="about-title">
        {text["title"]}
    </div>

    <div class="about-subtitle">
        {text["subtitle"]}
    </div>

</div>
""")


# ============================================================
# ABOUT CARDS
# ============================================================

st.html(f"""
<div class="about-grid">


    <div class="about-card">

        <h2>
            {text["project_title"]}
        </h2>

        <p>
            {text["project_text"]}
        </p>

    </div>


    <div class="about-card">

        <h2>
            {text["objective_title"]}
        </h2>

        <p>
            {text["objective_text"]}
        </p>

    </div>


    <div class="about-card">

        <h2>
            {text["technology_title"]}
        </h2>

        <p>
            {text["technology_text"]}
        </p>

    </div>


    <div class="about-card">

        <h2>
            {text["analysis_title"]}
        </h2>

        <p>
            {text["analysis_text"]}
        </p>

    </div>


</div>
""")


# ============================================================
# FOOTER
# ============================================================

st.html(f"""
<div class="about-footer">

    {text["footer"]}

</div>
""")