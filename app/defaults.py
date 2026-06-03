from app.schemas import (
    AboutStat,
    AboutUsCMSData,
    ContactCMSData,
    CourseItem,
    CoursesCMSData,
    DestinationItem,
    DestinationsCMSData,
    FooterCMSData,
    FooterLink,
    HomeCMSData,
    ServiceCard,
    StudyAbroadCMSData,
    TeamMember,
    TestimonialItem,
)


DEFAULT_HOME = HomeCMSData(
    heroBadge="YOUR TRUSTED EDUCATION PARTNER",
    heroTitle="Unlock Global Opportunities with V Five Education",
    heroSubtitle=(
        "Empowering students through expert Korean/Japanese language preparation, "
        "IELTS/PTE coaching, and premium university counseling."
    ),
    heroImageUrl="/student_hero.png",
    whoWeAreBadge="About Us",
    whoWeAreTitle="Who We Are",
    whoWeAreParagraph1=(
        "V Five Education Consultancy is a premier academic mentoring institution dedicated to "
        "facilitating international education journeys. We specialize in providing comprehensive "
        "support for students seeking to study in Korea, Japan, and Western nations."
    ),
    whoWeAreParagraph2=(
        "Our team of certified counselors and language experts ensures that every student receives "
        "a tailored roadmap, from language proficiency to visa approval, ensuring a seamless "
        "transition to their chosen global campus."
    ),
    whoWeAreLinkText="Learn about our mission",
    stat1Value="15+",
    stat1Title="Years of Experience",
    stat1Desc="Dedicated service in international academic placements.",
    stat2Value="98%",
    stat2Title="Visa Success Rate",
    stat2Desc="Proven track record for Korea, Japan, and Western nations.",
    servicesBadge="Our Services",
    servicesTitle="Our Dedicated Services",
    servicesSubtitle=(
        "We provide end-to-end assistance to ensure your educational journey is smooth, "
        "successful, and tailored to your career goals."
    ),
    services=[
        ServiceCard(
            title="Career Counselling",
            description=(
                "Expert guidance to help you choose the right course and destination based on "
                "your academic profile and future aspirations."
            ),
            linkText="Explore More",
            featured=False,
            icon="compass",
        ),
        ServiceCard(
            title="Test Preparation",
            description=(
                "Intensive coaching for IELTS, PTE, TOPIK, and JLPT with experienced instructors "
                "and state-of-the-art learning resources."
            ),
            linkText="Join Class",
            featured=True,
            icon="book-open",
        ),
        ServiceCard(
            title="Interview Assistance",
            description=(
                "Comprehensive mock interviews and communication workshops to prepare you for "
                "university and embassy interactions."
            ),
            linkText="View Details",
            featured=False,
            icon="users",
        ),
    ],
    featuredBadge="Programs",
    featuredTitle="Featured Courses",
    featuredSubtitle="Master a new language and open doors to world-class global universities.",
    featuredCourseIds=[1, 2, 3],
    testimonialsBadge="Testimonials",
    testimonialsTitle="Student Success Stories",
    contactBannerBadge="Get in Touch",
    contactBannerText=(
        "Our expert consultants are ready to guide your global education journey. "
        "Contact us today for personalized academic counseling."
    ),
    contactBannerImageUrl="/classroom_bg.png",
    inquiryFormTitle="Send an Inquiry",
    inquiryFormSubtitle=(
        "Fill out the form below and one of our expert education consultants will get back to you within 24 hours."
    ),
    testimonials=[
        TestimonialItem(
            id=1,
            name="Anish Thapa",
            location="Studying in Osaka, Japan",
            initials="AT",
            text=(
                "V Five Education Consultancy helped me clear my JLPT N4 exam in my first attempt. "
                "Their visa processing for Japan was incredibly smooth and transparent. Truly grateful!"
            ),
            featured=False,
        ),
        TestimonialItem(
            id=2,
            name="Priya Karki",
            location="EPS Korea Aspirant",
            initials="PK",
            text=(
                "The best Korean language classes in Kathmandu! The teachers at V Five are very patient "
                "and the mock tests are exactly like the real EPS-TOPIK exam. Highly recommended."
            ),
            featured=True,
        ),
        TestimonialItem(
            id=3,
            name="Ramesh Gurung",
            location="Global Scholar, Seoul",
            initials="RG",
            text=(
                "I was confused about studying abroad. The V Five counselling team gave me a clear path "
                "for South Korea. Their honesty and support are unmatched in Bagbazar."
            ),
            featured=False,
        ),
    ],
)

DEFAULT_COURSES = CoursesCMSData(
    title="Empower Your Future with Professional Education",
    subtitle=(
        "Providing expert language training, professional accounting courses, "
        "and university entrance preparation since 2010."
    ),
    items=[
        CourseItem(
            id=1,
            title="Korean Language (EPS & Student Visa)",
            category="Languages",
            categoryTag="LANGUAGE PROFICIENCY",
            description="Comprehensive training for EPS-TOPIK and student visa applicants at V Five Education.",
            duration="12 Weeks",
            mode="In-Person Classes",
            language="Korean Language",
            imageUrl="/korean_course.png",
            batchInfo="Batch Starts: 1st Nov",
        ),
        CourseItem(
            id=2,
            title="Japanese Language (N5 to N1)",
            category="Languages",
            categoryTag="LANGUAGE PROFICIENCY",
            description="Master Japanese for employment or higher education. Specialized courses for SSW and student visa.",
            duration="18 Weeks",
            mode="In-Person Classes",
            language="Japanese Language",
            imageUrl="/japanese_course.png",
            batchInfo="Daily Sessions Available",
        ),
        CourseItem(
            id=3,
            title="IELTS & PTE Preparation",
            category="Exam Prep",
            categoryTag="EXAM PREP",
            description="Intensive coaching with mock tests and personalized feedback for global admission success.",
            duration="8 Weeks",
            mode="Online/Virtual",
            language="English (IELTS/PTE)",
            imageUrl="/ielts_course.png",
            batchInfo="Free Mock Tests Included",
        ),
        CourseItem(
            id=4,
            title="Tuition Class (All Subjects)",
            category="Academic Support",
            categoryTag="ACADEMIC SUPPORT",
            description="Specialized subject support for school and college levels with experienced tutors.",
            duration="8 Weeks",
            mode="In-Person Classes",
            language="None",
            imageUrl="/classroom_bg.png",
            batchInfo="Daily Batches",
        ),
        CourseItem(
            id=5,
            title="Professional Accounting Training",
            category="Professional",
            categoryTag="PROFESSIONAL",
            description="Hands-on training in financial accounting and taxation for aspiring professionals.",
            duration="12 Weeks",
            mode="Hybrid Learning",
            language="None",
            imageUrl="/student_hero.png",
            batchInfo="Weekend Batch Available",
        ),
        CourseItem(
            id=6,
            title="Entrance Preparation",
            category="Academic Entry",
            categoryTag="ACADEMIC ENTRY",
            description="Coaching for national and international university entrance exams at V Five.",
            duration="12 Weeks",
            mode="Online/Virtual",
            language="None",
            imageUrl="/classroom_bg.png",
            batchInfo="Next Intake: Nov 1",
        ),
    ],
)

DEFAULT_DESTINATIONS = DestinationsCMSData(
    heroBadge="Expand Your Horizons",
    title="Your Gateway to Global Education",
    subtitle=(
        "Choose from our handpicked study destinations offering world-class training, "
        "high visa success rates, and excellent career paths."
    ),
    gridSectionTitle="Explore Your Future Campus",
    gridSectionSubtitle="Selected top-tier countries offering diverse academic excellence.",
    items=[
        DestinationItem(
            id=1,
            name="South Korea",
            tagline="Global Tech Hub and Rich Cultural Heritage.",
            badge="MOST POPULAR",
            highlights=["Affordable Tuition", "Part-Time Job Permit", "100% Scholarship Option"],
            imageUrl="/korean_course.png",
            flag="🇰🇷",
        ),
        DestinationItem(
            id=2,
            name="Japan",
            tagline="World-Class Engineering, Innovation, and Work Opportunities.",
            badge="SSW PATHWAY",
            highlights=["SSW Job Placement", "NAT/JLPT Coaching", "High Quality of Life"],
            imageUrl="/japanese_course.png",
            flag="🇯🇵",
        ),
        DestinationItem(
            id=3,
            name="United Kingdom",
            tagline="Centuries of Academic Prestige and Global Recognition.",
            badge="TOP RANKED",
            highlights=["2-Year Post Study Work", "Fast-Track Master's", "No IELTS Pathways"],
            imageUrl="/study_abroad_hero.png",
            flag="🇬🇧",
        ),
        DestinationItem(
            id=4,
            name="Canada",
            tagline="Welcoming Immigration Policies and High Standard of Living.",
            badge="PR PATHWAY",
            highlights=["PGWP Eligible", "Co-op Internships", "Permanent Residency Route"],
            imageUrl="/classroom_bg.png",
            flag="🇨🇦",
        ),
    ],
)

DEFAULT_STUDY_ABROAD = StudyAbroadCMSData(
    heroTitle="Global Opportunities Await You",
    heroSubtitle=(
        "Explore high-quality education systems, scholarship opportunities, "
        "and post-study work options with V Five Education."
    ),
    heroImageUrl="/study_abroad_hero.png",
    sectionTitle="Why Study Abroad?",
    sectionDesc=(
        "Embarking on a study abroad journey is a transformative experience that broadens academic, "
        "cultural, and career perspectives. Let us guide you at every step."
    ),
    scholarshipDesc=(
        "Comprehensive Admissions and Financial Aid support for meritorious students "
        "looking to study in top global universities."
    ),
    popularDestSubtitle=(
        "Choose from the top education hubs worldwide with tailored support for each region."
    ),
    featuredDestinationIds=[3, 2, 4, 5, 1],
    journeyTitle="Your Four-Step Journey to Global Success",
    journeyDesc=(
        "We've streamlined the application process to ensure a stress-free experience "
        "from your first consultation to your first day of class."
    ),
)

DEFAULT_ABOUT = AboutUsCMSData(
    heroBadge="Our Journey & Purpose",
    heroTitle="Empowering Your Global Dreams Since 2010",
    heroSubtitle=(
        "V Five Education Consultancy is dedicated to paving clear pathways for students seeking "
        "quality international education and professional career success."
    ),
    heroImageUrl="/student_hero.png",
    storyHighlights=[
        "Certified Career Counselors",
        "98% Visa Success Rate",
        "Affordable Language Prep",
        "50+ Global Partner Universities",
    ],
    storyImageUrl="/student_hero.png",
    storyOverlayValue="14+ Years",
    storyOverlayLabel="Of Trusted Counselling & Training",
    foundationsTitle="Our Core Strategy & Values",
    teamSubtitle=(
        "Experienced instructors, licensed counselors, and student advisors "
        "who support you at every milestone."
    ),
    ctaDesc=(
        "Schedule a call with our Senior Counselor to map out your language courses "
        "or higher education visa roadmap."
    ),
    storyParagraph1=(
        "Founded over a decade ago, V Five Education Consultancy has grown into a trusted beacon "
        "for students across Nepal. We bridge the gap between ambitious minds and world-class "
        "universities in countries like South Korea, Japan, United Kingdom, Canada, and Australia."
    ),
    storyParagraph2=(
        "Beyond study abroad counselling, we provide top-tier preparation classes for EPS-TOPIK, "
        "Japanese Language (NAT/JLPT), IELTS, and PTE. Our student-centric approach ensures you "
        "receive precise counseling, reliable document formatting, and direct visa processing guidance."
    ),
    stats=[
        AboutStat(value="10k+", label="Students Assisted"),
        AboutStat(value="98%", label="Visa Success Rate"),
        AboutStat(value="50+", label="Partner Universities"),
        AboutStat(value="15+", label="Expert Counselors"),
    ],
    teamMembers=[
        TeamMember(
            id=1,
            name="Ramesh K.C.",
            role="Managing Director",
            bio="15+ years of strategic leadership in educational immigration counseling.",
            imageUrl="/student_hero.png",
        ),
        TeamMember(
            id=2,
            name="Anita Shrestha",
            role="Senior Counselor",
            bio="Expert in Korean & Japanese visa guidelines and university options.",
            imageUrl="/student_writing.png",
        ),
        TeamMember(
            id=3,
            name="Bipin Gurung",
            role="Language Head (IELTS/PTE)",
            bio="Dedicated to helping students cross the band score requirements smoothly.",
            imageUrl="/student_hero.png",
        ),
        TeamMember(
            id=4,
            name="Sato Tanaka",
            role="Japanese Coordinator",
            bio="Native-level guidance for JLPT and cultural integration in Japan.",
            imageUrl="/student_writing.png",
        ),
    ],
    mission=(
        "To simplify the complex study abroad process by providing accurate, personalized counselling "
        "and excellent language preparation classes that unlock global opportunities."
    ),
    vision=(
        "To be recognized as the most transparent and successful educational consultancy in Nepal, "
        "fostering global capability and leadership within Nepalese youth."
    ),
    values=(
        "Trust, transparency, and students' best interests govern our counseling rules. "
        "We ensure realistic expectations and ethical compliance at every phase."
    ),
)

DEFAULT_CONTACT = ContactCMSData(
    whatsapp="+977 98012 34567",
    phone="+977 1 4412345 / 4412346",
    email="info@vfiveeducation.com",
    hours="Sunday - Friday: 9:00 AM - 6:00 PM | Saturday: Closed",
    location="Putalisadak, Kathmandu, Nepal | Main Educational Hub Building",
)

DEFAULT_FOOTER = FooterCMSData(
    brandTitle="About Us",
    description=(
        "V Five is a leading education consultancy dedicated to fulfilling your dreams of "
        "international education and career success through expert mentoring and unwavering support."
    ),
    quickLinksTitle="Quick Links",
    quickLinks=[
        FooterLink(label="Home", href="/"),
        FooterLink(label="About Us", href="/about"),
        FooterLink(label="Courses", href="/courses"),
        FooterLink(label="Destinations", href="/destinations"),
        FooterLink(label="Study Abroad", href="/study-abroad"),
        FooterLink(label="Contact Us", href="/contact"),
    ],
    supportTitle="Support",
    supportLinks=[
        FooterLink(label="Privacy Policy", href="#"),
        FooterLink(label="Terms of Service", href="#"),
        FooterLink(label="FAQ", href="#"),
        FooterLink(label="Career Guidance", href="/contact"),
    ],
    contactTitle="Contact Info",
    copyrightText="V Five Education Consultancy. All rights reserved.",
    taglinePrefix="Designed with Excellence for",
    taglineHighlight="Future Global Scholars",
)

def default_store() -> dict:
    return {
        "home": DEFAULT_HOME.model_dump(),
        "courses": DEFAULT_COURSES.model_dump(),
        "destinations": DEFAULT_DESTINATIONS.model_dump(),
        "studyAbroad": DEFAULT_STUDY_ABROAD.model_dump(),
        "about": DEFAULT_ABOUT.model_dump(),
        "contact": DEFAULT_CONTACT.model_dump(),
        "footer": DEFAULT_FOOTER.model_dump(),
    }
