from setuptools import setup

setup(
    name="gcp-bucket-to-mongo-collection",
    version="0.1",
    description="A Python package to transfer JSON files from Google Cloud Storage to MongoDB.",
    author="Pranjal Kar",
    author_email="pranjalkar99.work@gmail.com",
    url="https://github.com/yourusername/your_project",
    packages=["gcp-bucket-to-mongo-collection"],
    install_requires=[
        "google-cloud-storage",
        "pymongo",
        # Add other dependencies here
    ],
)
