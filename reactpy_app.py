import reactpy as rp
from PIL import Image, ImageDraw
from fpdf import FPDF
from io import BytesIO
import base64
from reactpy import html

# Function to generate a PDF file
def generate_pdf(name, title, company, email):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    pdf.cell(200, 10, txt=f"Name: {name}", ln=True)
    pdf.cell(200, 10, txt=f"Title: {title}", ln=True)
    pdf.cell(200, 10, txt=f"Company: {company}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {email}", ln=True)

    # Generate PDF content as a string
    pdf_output = pdf.output(dest='S').encode('latin1')  # encode to bytes using latin1

    # Convert PDF content to base64
    pdf_base64 = base64.b64encode(pdf_output).decode('utf-8')
    
    return pdf_base64

# Function to generate a PNG image
def generate_png(name, title, company, email):
    # Create a PNG image with Pillow
    img = Image.new('RGB', (300, 200), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((10, 10), f"Name: {name}", fill=(0, 0, 0))
    d.text((10, 30), f"Title: {title}", fill=(0, 0, 0))
    d.text((10, 50), f"Company: {company}", fill=(0, 0, 0))
    d.text((10, 70), f"Email: {email}", fill=(0, 0, 0))
    
    # Create a BytesIO object to store the image
    img_buffer = BytesIO()
    img.save(img_buffer, format='PNG')
    
    # Get the buffer content and encode it in base64
    img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')
    
    return img_base64

# Main component
@rp.component
def BusinessCardGenerator():
    name, set_name = rp.use_state("")
    title, set_title = rp.use_state("")
    company, set_company = rp.use_state("")
    email, set_email = rp.use_state("")
    theme, set_theme = rp.use_state("light")
    font_choice, set_font_choice = rp.use_state("Arial")

    themes = {
        "light": {"background": "#FFFFFF", "text_color": "#000000"},
        "dark": {"background": "#333333", "text_color": "#FFFFFF"},
        "professional": {"background": "#f4f4f4", "text_color": "#333333"},
        "creative": {"background": "#FFDEE9", "text_color": "#2B2B52"},
    }

    fonts = ["Arial", "Helvetica", "Times New Roman", "Courier New"]

    def update_preview():
        theme_colors = themes[theme]
        return f"""
        <div style="border: 1px solid #000; padding: 10px; width: 300px; background-color: {theme_colors['background']}; color: {theme_colors['text_color']}; font-family: {font_choice};">
            <h2>{name}</h2>
            <p>{title}</p>
            <p>{company}</p>
            <p>{email}</p>
        </div>
        """

    def download_handler(filename, file_content, mime_type):
        return rp.html.a(
            {"href": f"data:{mime_type};base64,{file_content}", "download": filename},
            f"Download {filename}"
        )

    return rp.html.div(
        {"style": {"display": "flex", "flexDirection": "column", "alignItems": "center", "padding": "20px"}},
        rp.html.h1("Business Card Generator"),

        # Input form
        rp.html.div(
            {"style": {"marginBottom": "10px"}},
            rp.html.input({
                "placeholder": "Name",
                "value": name,
                "on_change": lambda e: set_name(e["target"]["value"]),
                "style": {"margin": "5px"}
            }),
            rp.html.input({
                "placeholder": "Title",
                "value": title,
                "on_change": lambda e: set_title(e["target"]["value"]),
                "style": {"margin": "5px"}
            }),
            rp.html.input({
                "placeholder": "Company",
                "value": company,
                "on_change": lambda e: set_company(e["target"]["value"]),
                "style": {"margin": "5px"}
            }),
            rp.html.input({
                "placeholder": "Email",
                "value": email,
                "on_change": lambda e: set_email(e["target"]["value"]),
                "style": {"margin": "5px"}
            }),
        ),

        # Theme selector
        rp.html.div(
            {"style": {"marginBottom": "10px"}},
            rp.html.label("Theme:"),
            rp.html.select(
                {"on_change": lambda e: set_theme(e["target"]["value"])},
                [rp.html.option({"value": t}, t.capitalize()) for t in themes.keys()],
                {"style": {"margin": "5px"}}
            ),
        ),

        # Font selector
        rp.html.div(
            {"style": {"marginBottom": "10px"}},
            rp.html.label("Font:"),
            rp.html.select(
                {"on_change": lambda e: set_font_choice(e["target"]["value"])},
                [rp.html.option({"value": f}, f) for f in fonts],
                {"style": {"margin": "5px"}}
            ),
        ),

        # Download buttons
        rp.html.div(
            {"style": {"marginBottom": "10px"}},
            download_handler("business_card.png", generate_png(name, title, company, email), "image/png"),
            download_handler("business_card.pdf", generate_pdf(name, title, company, email), "application/pdf"),
        ),

        # Real-time preview
        rp.html.h3("Preview:"),
        rp.html.div(
            {
                "dangerouslySetInnerHTML": {"__html": update_preview()},
                "style": {"margin": "10px"}
            },
        ),
    )

# Development server for ReactPy
if __name__ == "__main__":
    rp.run_app(BusinessCardGenerator)
