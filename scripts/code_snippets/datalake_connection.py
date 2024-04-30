"""This module contains a basic Data Lake Handler class to connect and interact with the Data Lake.

Requirements:
    1. Modules: azure, python-dotenv.
    2. DefaultAzureCredential from azure.identity requires the installation of the Azure CLI 
       and the command 'az login' run in the terminal.
    3. A .env.datalake file containing the Azure account name as ACCOUNT_NAME=, currently set 
       as local to the module.
"""

from os import path
from azure.storage.blob import BlobServiceClient, ContentSettings
from azure.identity import DefaultAzureCredential
from dotenv import dotenv_values


class DataLakeHandler:
    """Provides methods to interact with the datalake."""

    def __init__(self):
        """Constructor for the DataLakeHandler class."""
        self.datalake_config = {
            **dotenv_values(".env.datalake")
        }  # Assumes your environment contains a key ACCOUNT_NAME

    def is_directory_clear(
        self, file_name: str, container_name: str, file_date: str
    ) -> bool:
        """Checks if the datalake directory is clear for a given filename based on container and date path.

        Args:
            file_name (str): The name of the file to check.
            container_name (str): The name of the datalake container.
            file_date (str): The date of the file for storage in the format dd/mm/yyyy. Refactor as required.

        Returns:
            bool: True if the directory is clear, False otherwise.
        """
        day, month, year = file_date.split(r"/")
        month = month.lstrip("0")
        account_name = self.datalake_config["ACCOUNT_NAME"]
        blob_path = f"bronze/y{year}/m{month}/d{day}/{file_name}"
        try:
            blob_service_client = BlobServiceClient(
                account_url=f"https://{account_name}.blob.core.windows.net",
                credential=DefaultAzureCredential(),
            )
            container_client = blob_service_client.get_container_client(container_name)
            blobs = container_client.list_blobs(name_starts_with=blob_path)
            if len(list(blobs)) == 0:
                return True
            else:
                return False
        except Exception as e:
            # Add exception handling code, e.g. with a logger.
            return False

    def _progress_callback(self, current: int, total: int) -> None:
        """Logs the progress of the file upload to the datalake by percentage.

        Args:
            current (int): current number of bytes sent
            total (int): total number of bytes to send
        """
        print(
            "Progress: %s%%", round((current / total) * 100, 2)
        )  # Example callback function to detail progress. Recommended to use with a logger.

    def move_file_to_datalake(
        self, file_path: str, datalake_container: str, file_date: str
    ) -> None:
        """Moves a file to the datalake

        Args:
            file_path (str): The path of the file to move.
            datalake_container (str): The name of the datalake container.
            file_date (str): The date of the file for storage in the format dd/mm/yyyy. Refactor as required.
        """

        day, month, year = file_date.split(r"/")
        month = month.lstrip("0")
        _, file_name = path.split(file_path)  # Extracts the file name from the path

        blob_path = f"bronze/y{year}/m{month}/d{day}/{file_name}"
        account_name = self.datalake_config["ACCOUNT_NAME"]
        container_name = datalake_container
        try:
            blob_service_client = BlobServiceClient(
                account_url=f"https://{account_name}.blob.core.windows.net",
                credential=DefaultAzureCredential(),
            )
            container_client = blob_service_client.get_container_client(container_name)
            assert self.is_directory_clear(file_name, container_name, file_date)

            with open(file_path, "rb") as data:
                container_client.upload_blob(
                    name=blob_path,
                    data=data,
                    content_settings=ContentSettings(
                        content_type="application/octet-stream"
                    ),
                    progress_hook=self._progress_callback,
                )
        except AssertionError:
            # Add exception handling code, e.g. with a logger.
            raise
        except Exception as e:
            # Add exception handling code, e.g. with a logger.
            raise
