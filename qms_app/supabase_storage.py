from supabase import create_client, Client

from django.conf import settings


class SupabaseStorage:
    def __init__(self):
        self.url: str = settings.SUPABASE_URL
        self.key: str = settings.SUPABASE_KEY
        self.client: Client = create_client(self.url, self.key)
        self.bucket_name: str = settings.SUPABASE_BUCKET

    def upload_file(self, file, file_name):
        """
        Uploads a file to the Supabase storage bucket.

        :param file: The file object to upload (InMemoryUploadedFile)
        :param file_name: The desired file name in the bucket
        :return: Response from Supabase API
        """
        try:
            # Upload the file to Supabase
            response = self.client.storage.from_(self.bucket_name).upload(file_name, file.read())
            
            # Log the response for debugging purposes
            print("Supabase upload response:", response)

            # Check if response has the expected attributes
            if hasattr(response, 'path') and hasattr(response, 'full_path'):
                return {
                    'path': response.path,
                    'full_path': response.full_path,
                }
            else:
                return {"error": "Upload failed, no path or full_path found in response."}
        except Exception as e:
            # Print the error message for debugging
            print("Error during upload:", str(e))
            return {"error": str(e)}

    def get_file_url(self, file_name):
        """
        Gets the public URL of a file in the bucket.

        :param file_name: The file name in the bucket
        :return: A dictionary containing the public URL or an error message
        """
        try:
            public_url = self.client.storage.from_(self.bucket_name).get_public_url(file_name)
            return {"publicUrl": public_url}
        except Exception as e:
            return {"error": str(e)}
