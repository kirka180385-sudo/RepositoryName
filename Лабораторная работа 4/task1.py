if __name__ == "__main__":
    # Write your solution here
    pass
class Nuu:
    def __init__(self, pages, tyr):
        from typing import List, Optional, Dict, Any
        from datetime import datetime

        class SocialMedia:
            """
            Base class representing a generic social media platform.

            Attributes:
                name (str): Name of the social media platform
                _user_count (int): Number of active users (protected attribute)
                _founded_year (int): Year the platform was founded
                content_types (List[str]): Types of content supported by the platform
            """

            def __init__(self, name: str, user_count: int, founded_year: int, content_types: List[str]) -> None:
                """
                Initialize a SocialMedia instance.

                Args:
                    name: Name of the platform
                    user_count: Number of active users
                    founded_year: Year the platform was founded
                    content_types: List of content types supported
                """
                self.name = name
                self._user_count = user_count  # Protected attribute - internal use only
                self._founded_year = founded_year  # Protected attribute - should not be modified directly
                self.content_types = content_types

            def __str__(self) -> str:
                """
                Return a user-friendly string representation of the platform.

                Returns:
                    A readable description of the platform
                """
                return f"{self.name} (Founded: {self._founded_year}) - {self._user_count:,} users"

            def __repr__(self) -> str:
                """
                Return a detailed string representation for debugging.

                Returns:
                    A string that would recreate the object when passed to eval()
                """
                return (f"SocialMedia(name='{self.name}', user_count={self._user_count}, "
                        f"founded_year={self._founded_year}, content_types={self.content_types})")

            def get_platform_age(self) -> int:
                """
                Calculate the age of the platform.

                Returns:
                    Number of years since platform was founded
                """
                current_year = datetime.now().year
                return current_year - self._founded_year

            def estimate_engagement_rate(self) -> float:
                """
                Estimate average engagement rate for the platform.

                This is a base implementation that provides a generic calculation.

                Returns:
                    Estimated engagement rate as percentage
                """
                # Base calculation: assuming 30% of users are active daily
                return 30.0

            def add_content_type(self, content_type: str) -> None:
                """
                Add a new content type to the platform.

                Args:
                    content_type: New content type to add
                """
                if content_type not in self.content_types:
                    self.content_types.append(content_type)

            def remove_content_type(self, content_type: str) -> bool:
                """
                Remove a content type from the platform.

                Args:
                    content_type: Content type to remove

                Returns:
                    True if removed successfully, False if not found
                """
                if content_type in self.content_types:
                    self.content_types.remove(content_type)
                    return True
                return False

        class TikTok(SocialMedia):
            """
            Derived class representing TikTok platform.

            TikTok is a short-form video platform that extends SocialMedia with
            platform-specific features like trending sounds and video duration limits.

            Attributes:
                _trending_sounds (List[str]): Current trending sounds (private)
                _max_video_duration (int): Maximum video duration in seconds
                _music_library_size (int): Number of songs in the music library
            """

            def __init__(self, user_count: int, founded_year: int,
                         max_video_duration: int, music_library_size: int) -> None:
                """
                Initialize a TikTok instance.

                Args:
                    user_count: Number of active users
                    founded_year: Year the platform was founded
                    max_video_duration: Maximum video duration in seconds
                    music_library_size: Number of songs in the music library
                """
                # Extend base class constructor with TikTok-specific content types
                content_types = ["short_video", "live_stream", "duet", "stitch"]
                super().__init__("TikTok", user_count, founded_year, content_types)

                self._max_video_duration = max_video_duration  # Private attribute
                self._music_library_size = music_library_size  # Private attribute
                self._trending_sounds: List[str] = []  # Private attribute

            def __str__(self) -> str:
                """
                Return a user-friendly string representation for TikTok.

                Returns:
                    A readable description of TikTok with platform-specific details
                """
                # Override to include TikTok-specific information
                return (f"TikTok (Founded: {self._founded_year}) - {self._user_count:,} users | "
                        f"Max Duration: {self._max_video_duration}s | "
                        f"Music Library: {self._music_library_size:,} songs")

            def __repr__(self) -> str:
                """
                Return a detailed string representation for debugging TikTok.

                Returns:
                    A string that would recreate the TikTok object when passed to eval()
                """
                return (f"TikTok(user_count={self._user_count}, founded_year={self._founded_year}, "
                        f"max_video_duration={self._max_video_duration}, "
                        f"music_library_size={self._music_library_size})")

            def estimate_engagement_rate(self) -> float:
                """
                Estimate engagement rate specifically for TikTok.

                Reason for override: TikTok has higher engagement rates due to its
                algorithm-driven feed and short-form content format. The base class
                estimate of 30% is too conservative for this platform.

                Returns:
                    Estimated engagement rate as percentage
                """
                # TikTok typically has 40-50% engagement rate
                return 45.0

            def get_max_video_duration(self) -> int:
                """
                Get the maximum video duration allowed.

                Returns:
                    Maximum video duration in seconds
                """
                return self._max_video_duration

            def set_max_video_duration(self, duration: int) -> None:
                """
                Set the maximum video duration.

                Args:
                    duration: New maximum duration in seconds

                Raises:
                    ValueError: If duration is not positive
                """
                if duration <= 0:
                    raise ValueError("Duration must be positive")
                self._max_video_duration = duration

            def update_trending_sounds(self, sounds: List[str]) -> None:
                """
                Update the list of trending sounds.

                Args:
                    sounds: New list of trending sounds
                """
                self._trending_sounds = sounds.copy()

            def get_trending_sounds(self) -> List[str]:
                """
                Get current trending sounds.

                Returns:
                    Copy of trending sounds list
                """
                return self._trending_sounds.copy()

        class LinkedIn(SocialMedia):
            """
            Derived class representing LinkedIn platform.

            LinkedIn is a professional networking platform that extends SocialMedia
            with career-oriented features like job postings and professional skills.

            Attributes:
                _job_postings (int): Number of active job postings (private)
                _premium_users (int): Number of premium subscribers (private)
                _industries (List[str]): Industries covered by the platform
            """

            def __init__(self, user_count: int, founded_year: int,
                         job_postings: int, premium_users: int, industries: List[str]) -> None:
                """
                Initialize a LinkedIn instance.

                Args:
                    user_count: Number of active users
                    founded_year: Year the platform was founded
                    job_postings: Number of active job postings
                    premium_users: Number of premium subscribers
                    industries: List of industries covered
                """
                # Extend base class constructor with LinkedIn-specific content types
                content_types = ["articles", "job_postings", "certifications", "recommendations"]
                super().__init__("LinkedIn", user_count, founded_year, content_types)

                self._job_postings = job_postings  # Private attribute
                self._premium_users = premium_users  # Private attribute
                self.industries = industries  # Public attribute

            def __str__(self) -> str:
                """
                Return a user-friendly string representation for LinkedIn.

                Returns:
                    A readable description of LinkedIn with platform-specific details
                """
                # Override to include LinkedIn-specific information
                premium_percentage = (self._premium_users / self._user_count) * 100 if self._user_count > 0 else 0
                return (f"LinkedIn (Founded: {self._founded_year}) - {self._user_count:,} users | "
                        f"{self._job_postings:,} jobs | "
                        f"{premium_percentage:.1f}% premium users")

            def __repr__(self) -> str:
                """
                Return a detailed string representation for debugging LinkedIn.

                Returns:
                    A string that would recreate the LinkedIn object when passed to eval()
                """
                return (f"LinkedIn(user_count={self._user_count}, founded_year={self._founded_year}, "
                        f"job_postings={self._job_postings}, premium_users={self._premium_users}, "
                        f"industries={self.industries})")

            def estimate_engagement_rate(self) -> float:
                """
                Estimate engagement rate specifically for LinkedIn.

                Reason for override: LinkedIn is a professional network with lower
                daily engagement but higher quality interactions. The base class
                estimate of 30% is too high for this platform's usage patterns.

                Returns:
                    Estimated engagement rate as percentage
                """
                # LinkedIn typically has 15-20% engagement rate
                return 18.0

            def get_job_postings(self) -> int:
                """
                Get number of active job postings.

                Returns:
                    Number of active job postings
                """
                return self._job_postings

            def add_job_posting(self) -> None:
                """
                Increment job postings count by 1.

                This method demonstrates method inheritance from base class pattern.
                """
                self._job_postings += 1

            def get_premium_percentage(self) -> float:
                """
                Calculate percentage of premium users.

                Returns:
                    Percentage of users with premium subscription
                """
                if self._user_count == 0:
                    return 0.0
                return (self._premium_users / self._user_count) * 100

