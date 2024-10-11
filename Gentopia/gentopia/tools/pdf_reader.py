from gentopia.tools.basetool import *
from typing import AnyStr
import PyPDF2
import asyncio
import requests
from io import BytesIO

class PDFReaderArgs(BaseModel):
    file_path: str

class PDFReader(BaseTool):
    name = "pdf_reader"
    description = ("Reads a PDF file and returns the text content."
                   "Useful for summarizing papers."
                   )
    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def read_pdf_from_url(self, url):
        # Send a request to get the PDF
        response = requests.get(url, stream=True)
        print(f"Fetching PDF from {url}")
        
        if response.status_code != 200:
            raise Exception(f"Failed to retrieve PDF: Status code {response.status_code}")

        # Use BytesIO to handle the PDF in memory
        pdf_stream = BytesIO(response.content)

        return pdf_stream

    # PDF reading function
    def extract_text_from_pdf(self, pdf_stream):
        try:
            # Create a PDF reader object from the stream
            reader = PyPDF2.PdfReader(pdf_stream)
            text = []
            for page in reader.pages:
                text.append(page.extract_text())
            return '\n'.join(text)
        except Exception as e:
            return str(e)

    def _run(self, file_path: AnyStr, task_name: str = "") -> str:
        # Check if the input is a URL or a local file
        if file_path.startswith("http"):
            print(f"Reading PDF from URL: {file_path}")
            pdf_stream = self.read_pdf_from_url(file_path)
            return self.extract_text_from_pdf(pdf_stream)
        else:
            print(f"Reading local PDF file: {file_path}")
            with open(file_path, 'rb') as file:
                return self.extract_text_from_pdf(file)

    async def _arun(self, file_path: AnyStr) -> str:
        return await asyncio.to_thread(self._run, file_path)



if __name__ == "__main__":
    pdf_reader = PDFReader()

    result = pdf_reader._run("https://arxiv.org/pdf/2308.04030")
    print(result)