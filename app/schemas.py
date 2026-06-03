from datetime import datetime

from pydantic import BaseModel, Field


class TestimonialItem(BaseModel):
    id: int
    name: str
    location: str
    initials: str
    text: str
    featured: bool


class ServiceCard(BaseModel):
    title: str
    description: str
    linkText: str
    featured: bool = False
    icon: str = "compass"


class HomeCMSData(BaseModel):
    heroBadge: str
    heroTitle: str
    heroSubtitle: str
    heroImageUrl: str

    whoWeAreBadge: str = "About Us"
    whoWeAreTitle: str = "Who We Are"
    whoWeAreParagraph1: str = ""
    whoWeAreParagraph2: str = ""
    whoWeAreLinkText: str = "Learn about our mission"
    stat1Value: str = "15+"
    stat1Title: str = "Years of Experience"
    stat1Desc: str = ""
    stat2Value: str = "98%"
    stat2Title: str = "Visa Success Rate"
    stat2Desc: str = ""

    servicesBadge: str = "Our Services"
    servicesTitle: str = "Our Dedicated Services"
    servicesSubtitle: str = ""
    services: list[ServiceCard] = Field(default_factory=list)

    featuredBadge: str = "Programs"
    featuredTitle: str = "Featured Courses"
    featuredSubtitle: str = ""
    featuredCourseIds: list[int]

    testimonialsBadge: str = "Testimonials"
    testimonialsTitle: str = "Student Success Stories"
    testimonials: list[TestimonialItem]

    contactBannerBadge: str = "Get in Touch"
    contactBannerText: str = ""
    contactBannerImageUrl: str = "/classroom_bg.png"
    inquiryFormTitle: str = "Send an Inquiry"
    inquiryFormSubtitle: str = ""


class FooterLink(BaseModel):
    label: str
    href: str


class FooterCMSData(BaseModel):
    brandTitle: str = "About Us"
    description: str = ""
    quickLinksTitle: str = "Quick Links"
    quickLinks: list[FooterLink] = Field(default_factory=list)
    supportTitle: str = "Support"
    supportLinks: list[FooterLink] = Field(default_factory=list)
    contactTitle: str = "Contact Info"
    copyrightText: str = "V Five Education Consultancy. All rights reserved."
    taglinePrefix: str = "Designed with Excellence for"
    taglineHighlight: str = "Future Global Scholars"


class CourseItem(BaseModel):
    id: int
    title: str
    category: str
    categoryTag: str
    description: str
    duration: str
    mode: str
    language: str
    imageUrl: str
    batchInfo: str


class CoursesCMSData(BaseModel):
    title: str
    subtitle: str
    items: list[CourseItem]


class DestinationItem(BaseModel):
    id: int
    name: str
    tagline: str
    badge: str
    highlights: list[str]
    imageUrl: str = "/classroom_bg.png"
    flag: str = "🌐"


class DestinationsCMSData(BaseModel):
    heroBadge: str = "Expand Your Horizons"
    title: str
    subtitle: str
    gridSectionTitle: str = "Explore Your Future Campus"
    gridSectionSubtitle: str = ""
    items: list[DestinationItem]


class StudyAbroadCMSData(BaseModel):
    heroTitle: str
    heroSubtitle: str
    heroImageUrl: str
    sectionTitle: str
    sectionDesc: str
    scholarshipBadge: str = "Merit-Based Scholarships"
    scholarshipTitle: str = "Up to 100% Tuition Waiver"
    scholarshipDesc: str = ""
    scholarshipButtonText: str = "Check Your Eligibility"
    popularDestTitle: str = "Popular Destinations"
    popularDestSubtitle: str = ""
    featuredDestinationIds: list[int] = Field(default_factory=lambda: [3, 2, 4, 5, 1])
    journeyBadge: str = "How It Works"
    journeyTitle: str = "Your Four-Step Journey to Global Success"
    journeyDesc: str = ""


class AboutStat(BaseModel):
    value: str
    label: str


class TeamMember(BaseModel):
    id: int
    name: str
    role: str
    bio: str
    imageUrl: str


class AboutUsCMSData(BaseModel):
    heroBadge: str = "Our Journey & Purpose"
    heroTitle: str
    heroSubtitle: str
    heroImageUrl: str
    storyBadge: str = "Who We Are"
    storyTitle: str = "Leading the Way in Educational Excellence"
    storyParagraph1: str = ""
    storyParagraph2: str = ""
    storyHighlights: list[str] = Field(default_factory=list)
    storyImageUrl: str = ""
    storyOverlayValue: str = "14+ Years"
    storyOverlayLabel: str = "Of Trusted Counselling & Training"
    stats: list[AboutStat] = Field(default_factory=list)
    foundationsBadge: str = "Foundations"
    foundationsTitle: str = "Our Core Strategy & Values"
    teamBadge: str = "Our Experts"
    teamTitle: str = "Meet Our Dedicated Leadership Team"
    teamSubtitle: str = ""
    teamMembers: list[TeamMember] = Field(default_factory=list)
    ctaBadge: str = "Consult with Us"
    ctaTitle: str = "Have Questions About Getting Started?"
    ctaDesc: str = ""
    ctaButtonText: str = "Contact Us Now"
    ctaImageUrl: str = "/classroom_bg.png"
    mission: str
    vision: str
    values: str


class ContactCMSData(BaseModel):
    whatsapp: str
    phone: str
    email: str
    hours: str
    location: str


class LoginRequest(BaseModel):
    email: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class AdminUserResponse(BaseModel):
    id: int
    email: str
    name: str
    role: str
    created_at: datetime


class AdminUserCreate(BaseModel):
    email: str
    password: str
    name: str = ""


class AdminMeResponse(BaseModel):
    id: int
    email: str
    name: str
    role: str
    authenticated: bool = True


class HealthResponse(BaseModel):
    status: str = "ok"
    service: str = "vfive-backend"
    database: str = "connected"


class UploadResponse(BaseModel):
    url: str
    public_id: str


class UploadStatusResponse(BaseModel):
    configured: bool
    max_upload_mb: int


class InquiryCreate(BaseModel):
    name: str
    phone: str
    email: str
    course: str
    message: str


class InquiryResponse(BaseModel):
    id: int
    name: str
    phone: str
    email: str
    course: str
    message: str
    created_at: datetime


class InquirySubmitResponse(BaseModel):
    ok: bool = True
    message: str = "Inquiry received. We will contact you within 24 hours."
