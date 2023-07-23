import pytest

from app import file_operations


@pytest.fixture()
def updated_class():
    file_operations.Csv._folder_path = "./tests/test_data_csv"
    return file_operations.Csv


def test_get_all_files_all_columns(updated_class):
    assert updated_class.get_all_files_all_columns() == {
        "test.csv": {
            "columns": [
                "VIN (1-10)",
                "County",
                "City",
                "State",
                "Postal Code",
                "Model Year",
                "Make",
                "Model",
                "Electric Vehicle Type",
                "Clean Alternative Fuel Vehicle (CAFV) Eligibility",
                "Electric Range",
                "Base MSRP",
                "Legislative District",
                "DOL Vehicle ID",
                "Vehicle Location",
                "Electric Utility",
                "2020 Census Tract",
            ]
        }
    }
