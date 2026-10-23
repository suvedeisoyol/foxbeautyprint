import streamlit as st

st.set_page_config(page_title="Product Label Generator", layout="centered")

st.title("🏷️ 3-in-1 A4 Product Label Generator")
st.info("💡 **How to use:** Click and type directly inside any of the boxes to edit. Each label has a full border line for easy cutting.")

# Combined HTML/CSS template to stack 3 fully-bordered cards on an A4 sheet
label_iframe_html = """
<!DOCTYPE html>
<html>
<head>
    <style>
        /* Force page size and strip browser-enforced padding */
        @page {
            size: A4 portrait;
            margin: 0;
        }
        
        body {
            margin: 0;
            padding: 0;
            background-color: #f0f2f6;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        /* SCREEN PREVIEW CONTAINER */
        .wrapper {
            width: 100%;
            max-width: 600px;
            margin-top: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 15px;
        }

        /* GRID CHASSIS: Stacks the 3 cards perfectly together */
        .labels-grid {
            display: flex;
            flex-direction: column;
            width: 210mm;
            height: 297mm; /* Full A4 Height */
            background-color: #ffffff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.15);
            box-sizing: border-box;
            padding: 2mm; /* Small safety padding so outer lines don't get clipped by printers */
            gap: 2mm;      /* Small space between boxes */
        }

        /* INDIVIDUAL LABEL: Scaled down slightly to fit borders nicely on 1/3 page */
        .label-card {
            width: 100%;
            height: 95mm; 
            box-sizing: border-box;
            border: 2px dashed #1A202C; /* Dashed line on screen */
            border-radius: 4px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            background-color: #ffffff;
        }

        /* Editing interactive focus highlights */
        .editable-field {
            width: 90%;
            padding: 4px;
            border-radius: 4px;
            transition: all 0.2s ease;
        }
        .editable-field:hover {
            background-color: #FEFCBF;
            outline: 1px dashed #D69E2E;
            cursor: text;
        }
        .editable-field:focus {
            background-color: #ffffff;
            outline: 2px solid #3182CE;
        }

        .title {
            font-size: 28pt;
            font-weight: 700;
            color: #1A202C;
            margin-bottom: 5px;
        }

        .divider {
            width: 70%;
            border: none;
            border-top: 2px solid #E2E8F0;
            margin: 10px 0;
        }

        .price {
            font-size: 48pt;
            font-weight: 900;
            color: #E53E3E;
        }

        .print-btn {
            background-color: #FF4B4B;
            color: white;
            border: none;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 8px;
            cursor: pointer;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .print-btn:hover {
            background-color: #E03E3E;
        }

        /* PRINT INTERACTION SYSTEM CONFIGURATION */
        @media print {
            .print-btn {
                display: none !important;
            }
            body {
                background-color: #ffffff !important;
            }
            .wrapper {
                margin: 0 !important;
                padding: 0 !important;
                max-width: none !important;
            }
            .labels-grid {
                box-shadow: none !important;
                position: absolute !important;
                left: 0 !important;
                top: 0 !important;
                padding: 2mm !important;
            }
            .label-card {
                /* Turns into a crisp, solid black bounding box around each label when printed */
                border: 2px solid #000000 !important; 
            }
            .editable-field {
                outline: none !important;
                background-color: transparent !important;
            }
            .price {
                color: #000000 !important; /* Rich black printing ink */
            }
        }
    </style>
</head>
<body>

    <div class="wrapper">
        <button class="print-btn" onclick="window.print()">🖨️ Print All 3 Labels</button>
        
        <div class="labels-grid">
            <!-- LABEL 1 -->
            <div class="label-card">
                <div class="title editable-field" contenteditable="true">Product Name One</div>
                <hr class="divider">
                <div class="price editable-field" contenteditable="true">$19.99</div>
            </div>
            
            <!-- LABEL 2 -->
            <div class="label-card">
                <div class="title editable-field" contenteditable="true">Product Name Two</div>
                <hr class="divider">
                <div class="price editable-field" contenteditable="true">$24.99</div>
            </div>
            
            <!-- LABEL 3 -->
            <div class="label-card">
                <div class="title editable-field" contenteditable="true">Product Name Three</div>
                <hr class="divider">
                <div class="price editable-field" contenteditable="true">$14.50</div>
            </div>
        </div>
    </div>

</body>
</html>
"""

# Render full stacked layout template
st.components.v1.html(label_iframe_html, height=1250, scrolling=False)
