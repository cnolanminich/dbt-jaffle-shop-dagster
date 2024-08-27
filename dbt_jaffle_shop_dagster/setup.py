from setuptools import find_packages, setup

setup(
    name="dbt_jaffle_shop_dagster",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        "dbt_jaffle_shop_dagster": [
            "dbt-project/**/*",
        ],
    },
    install_requires=[
        "dagster==1.8.3",
        "dagster-cloud==1.8.3",
        "dagster-dbt",
        "dbt-duckdb<1.9",
        "grpcio-health-checking==1.66.0"
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

