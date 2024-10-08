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
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dbt-duckdb",
        "dbt-core",
    ],
    extras_require={
        "dev": [
            "dagster-webserver",
        ]
    },
)

