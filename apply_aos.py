import re

path = r'd:\kajal private\project works\Godrej Brooklyn Avenues ( Kukkatpally)\index.html'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add AOS CSS in head
if 'aos.css' not in content:
    content = content.replace('<!-- Custom CSS -->', '<!-- AOS CSS -->\n    <link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">\n    <!-- Custom CSS -->')

# Add AOS JS at the bottom
if 'aos.js' not in content:
    content = content.replace('<!-- Scripts -->', '<!-- AOS Script -->\n    <script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>\n    <script>\n        AOS.init({\n            duration: 800,\n            once: true,\n            offset: 100\n        });\n    </script>\n    <!-- Scripts -->')

# Replace reveal with AOS
content = content.replace('class="col-lg-5 offset-lg-1 mt-5 mt-lg-0 reveal"', 'class="col-lg-5 offset-lg-1 mt-5 mt-lg-0" data-aos="fade-left"')
content = content.replace('class="text-center mb-5 section-header reveal"', 'class="text-center mb-5 section-header" data-aos="fade-up"')
content = content.replace('class="col-lg-4 reveal" style="transition-delay: 0.1s;"', 'class="col-lg-4" data-aos="fade-up" data-aos-delay="100"')
content = content.replace('class="col-lg-4 reveal" style="transition-delay: 0.2s;"', 'class="col-lg-4" data-aos="fade-up" data-aos-delay="200"')
content = content.replace('class="col-lg-4 reveal"', 'class="col-lg-4" data-aos="fade-up"')
content = content.replace('class="col-lg-6 reveal mt-5"', 'class="col-lg-6 mt-5" data-aos="fade-up"')
content = content.replace('class="col-12 reveal mt-5"', 'class="col-12 mt-5" data-aos="fade-up"')
content = content.replace('class="row justify-content-center reveal"', 'class="row justify-content-center" data-aos="zoom-in"')
content = content.replace('class="col-md-6 reveal" style="transition-delay: 0.1s;"', 'class="col-md-6" data-aos="fade-up" data-aos-delay="100"')
content = content.replace('class="col-md-6 reveal" style="transition-delay: 0.2s;"', 'class="col-md-6" data-aos="fade-up" data-aos-delay="200"')
content = content.replace('class="col-md-6 reveal" style="transition-delay: 0.3s;"', 'class="col-md-6" data-aos="fade-up" data-aos-delay="300"')
content = content.replace('class="col-md-6 reveal"', 'class="col-md-6" data-aos="fade-up"')
content = content.replace('class="col-lg-5 reveal"', 'class="col-lg-5" data-aos="fade-right"')
content = content.replace('class="col-lg-7 reveal" style="transition-delay: 0.1s;"', 'class="col-lg-7" data-aos="fade-left"')
content = content.replace('class="container position-relative z-index-2 reveal"', 'class="container position-relative z-index-2" data-aos="fade-up"')

# Clean up remaining reveals if any
content = re.sub(r'\s*reveal\s*', ' ', content)

# Add image zoom wrappers
content = content.replace('<img src="images/page_2.png" alt="Master Plan" class="img-fluid flex-grow-1" style="object-fit: cover;">', '<div class="image-zoom-container h-100"><img src="images/page_2.png" alt="Master Plan" class="img-fluid w-100 h-100" style="object-fit: cover;"></div>')
content = content.replace('<img src="images/page_5.png" alt="Vicinity Map" class="img-fluid flex-grow-1" style="object-fit: cover;">', '<div class="image-zoom-container h-100"><img src="images/page_5.png" alt="Vicinity Map" class="img-fluid w-100 h-100" style="object-fit: cover;"></div>')

content = content.replace('<img src="images/page_7.png" alt="3BHK West facing 1810 sft" class="img-fluid rounded">', '<div class="image-zoom-container"><img src="images/page_7.png" alt="3BHK West facing 1810 sft" class="img-fluid rounded"></div>')
content = content.replace('<img src="images/page_8.png" alt="3BHK East facing 2200SFT" class="img-fluid rounded">', '<div class="image-zoom-container"><img src="images/page_8.png" alt="3BHK East facing 2200SFT" class="img-fluid rounded"></div>')
content = content.replace('<img src="images/page_9.png" alt="WEST FACING APARTMENT - 1899 Sft 3 BHK - 3T" class="img-fluid rounded">', '<div class="image-zoom-container"><img src="images/page_9.png" alt="WEST FACING APARTMENT - 1899 Sft 3 BHK - 3T" class="img-fluid rounded"></div>')
content = content.replace('<img src="images/page_10.png" alt="4BHK west facing 3200 sft" class="img-fluid rounded">', '<div class="image-zoom-container"><img src="images/page_10.png" alt="4BHK west facing 3200 sft" class="img-fluid rounded"></div>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated successfully!')
