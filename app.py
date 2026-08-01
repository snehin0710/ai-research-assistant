"""
Application entry point.
"""

from src.services.research_service import ResearchService


def main() -> None:
    """
    Run the application.
    """

    service = ResearchService()

    query = input("Enter your research question: ")

    print("\nGenerating response...\n")

    response = service.research(query)

    print(response)


if __name__ == "__main__":
    main()