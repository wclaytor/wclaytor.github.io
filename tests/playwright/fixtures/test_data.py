"""
test_data.py - Test data constants.

Centralizes expected values used in assertions for easy maintenance.
"""


class TestData:
    """Constants for test assertions."""
    
    # Site information
    SITE_NAME = "wclaytor.github.io"
    AUTHOR_NAME = "William Claytor"
    
    # Homepage content
    MASTHEAD_TITLE = "william claytor"
    TAGLINE_CONTAINS = "25 Years"
    SUBTITLE_CONTAINS = "Senior Software Engineer"
    
    # Expertise areas (exact titles)
    EXPERTISE_AREAS = [
        "Software Development",
        "Quality Assurance",
        "Test Automation",
    ]
    
    # Expected skill tags
    DEV_SKILLS = ["Java", ".NET", "Ruby", "Python", "JavaScript"]
    QA_SKILLS = ["Team Leadership", "CI/CD", "SDLC", "Test Strategy"]
    AUTOMATION_SKILLS = ["Selenium", "Playwright", "Gatling", "API Testing"]
    
    # Featured projects
    FEATURED_PROJECTS = [
        "Alpine Resume",
        "Alpine Markdown Presentation",
    ]
    
    # Experiment projects
    EXPERIMENT_PROJECTS = [
        "Background Transformer",
        "Dynamic Resume",
    ]
    
    # Contact information
    EMAIL = "wclaytor@fastmail.com"
    LINKEDIN_URL = "https://www.linkedin.com/in/billclaytor/"
    GITHUB_URL = "https://github.com/wclaytor"
    
    # Navigation
    NAV_LINKS = ["About", "Projects", "Contact", "Resume"]
    NAV_BRAND = "wclaytor.github.io"
    
    # Projects page
    PROJECTS_PAGE_TITLE = "Projects"
    PROJECTS_PAGE_SUBTITLE = "Explore creative web projects and experiments"
    
    # Page titles
    HOME_PAGE_TITLE_CONTAINS = "William Claytor"
    RESUME_PAGE_TITLE_CONTAINS = "Resume"
    PROJECTS_PAGE_TITLE_CONTAINS = "Projects"
    
    # Accessibility
    SKIP_LINK_TEXT = "Skip to main content"
    
    # Copyright
    COPYRIGHT_START_YEAR = "2023"
    
    @classmethod
    def all_nav_links(cls) -> list[str]:
        """Get all expected navigation links."""
        return cls.NAV_LINKS.copy()
    
    @classmethod
    def all_featured_projects(cls) -> list[str]:
        """Get all featured project names."""
        return cls.FEATURED_PROJECTS.copy()
    
    @classmethod
    def all_experiment_projects(cls) -> list[str]:
        """Get all experiment project names."""
        return cls.EXPERIMENT_PROJECTS.copy()
