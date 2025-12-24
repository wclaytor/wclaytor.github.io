"""
urls.py - URL constants for tests.

Centralizes all URLs used in tests for easy maintenance.
"""


class URLs:
    """URL constants for the site."""
    
    # Main pages
    HOME = "/"
    PROJECTS = "/projects/"
    PROJECTS_INDEX = "/projects/index.html"
    RESUME = "/assets/resume/william_claytor_resume.html"
    
    # Featured projects
    ALPINE_RESUME = "/projects/alpine-resume/releases/20251214/index.html"
    ALPINE_RESUME_README = "/projects/alpine-resume/releases/20251214/README.html"
    ALPINE_PRESENTATION = "/projects/alpine-markdown-presentation/index.html"
    ALPINE_PRESENTATION_README = "/projects/alpine-markdown-presentation/README.html"
    
    # Experiment projects
    BACKGROUND_TRANSFORMER = "/projects/alpine-background-transformer/index.html"
    BACKGROUND_TRANSFORMER_README = "/projects/alpine-background-transformer/README.html"
    DYNAMIC_RESUME = "/projects/dynamic-resume/releases/v2.3/william_claytor_resume.html"
    DYNAMIC_RESUME_README = "/projects/dynamic-resume/releases/v2.3/README.html"
    
    # Other projects
    ALPINE_WAVES = "/projects/alpine-waves/index.html"
    ALPINE_ALGORITHMIC_ART = "/projects/alpine-algorithmic-art/index.html"
    AMBIENT_BEAT_NEXUS = "/projects/ambient-beat-nexus/index.html"
    
    # Page anchors (for homepage)
    ABOUT_ANCHOR = "/#about"
    PROJECTS_ANCHOR = "/#projects"
    CONTACT_ANCHOR = "/#contact"
    
    # External links
    LINKEDIN = "https://www.linkedin.com/in/billclaytor/"
    GITHUB = "https://github.com/wclaytor"
    
    @classmethod
    def all_pages(cls) -> list[str]:
        """
        Get all internal page URLs for smoke testing.
        
        Returns:
            List of all page paths
        """
        return [
            cls.HOME,
            cls.PROJECTS,
            cls.RESUME,
            cls.ALPINE_RESUME,
            cls.ALPINE_PRESENTATION,
            cls.BACKGROUND_TRANSFORMER,
        ]
    
    @classmethod
    def critical_pages(cls) -> list[str]:
        """
        Get critical page URLs that must always work.
        
        Returns:
            List of critical page paths
        """
        return [
            cls.HOME,
            cls.PROJECTS,
            cls.RESUME,
        ]
