from distutils.core import setup

setup(
    name="Speedloris",
    py_modules=["speedloris"],
    entry_points={"console_scripts": ["speedloris=speedloris:main"]},
    version="0.2.6",
    description="High bandwidth DDoS tool. Speedloris rewrite in Python.",
    author="Naveenventure",
    url="https://github.com/BuduruNaveen/Speedloris",
    keywords=["Ddos", "http", "speedloris"],
    license="MIT",
)
