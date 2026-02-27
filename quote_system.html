<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Brothers EGY - Professional Quotation System</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary: #04509D;
            --secondary: #2c3e50;
            --accent: #e67e22;
            --bg: #f4f7f9;
        }

        body { font-family: 'Segoe UI', sans-serif; background: var(--bg); margin: 0; padding: 20px; }
        
        /* Control Panel Styles */
        .setup-container { max-width: 900px; margin: 0 auto; background: white; padding: 30px; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.1); }
        .header-ui { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid var(--primary); padding-bottom: 15px; margin-bottom: 25px; }
        
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 20px; margin-bottom: 20px; }
        label { display: block; font-size: 11px; font-weight: 800; color: #555; text-transform: uppercase; margin-bottom: 5px; }
        input, select { width: 100%; padding: 12px; border: 1px solid #ddd; border-radius: 8px; box-sizing: border-box; }
        
        .btn-generate { background: var(--primary); color: white; border: none; padding: 15px 40px; border-radius: 50px; font-weight: bold; cursor: pointer; width: 100%; font-size: 16px; transition: 0.3s; }
        .btn-generate:hover { background: #033a75; transform: translateY(-2px); }

        /* A4 Quotation Styles */
        #quotationOutput { display: none; margin-top: 40px; }
        .a4-quote { 
            width: 210mm; min-height: 297mm; padding: 20mm; margin: 0 auto; 
            background: white; box-shadow: 0 0 20px rgba(0,0,0,0.2); position: relative;
            color: #333; line-height: 1.5; font-size: 10pt;
        }

        .quote-header { display: flex; justify-content: space-between; margin-bottom: 40px; }
        .company-meta { text-align: right; font-size: 9pt; color: #666; }
        
        .client-bar { background: var(--primary); color: white; padding: 15px; border-radius: 8px; display: flex; justify-content: space-between; margin-bottom: 30px; }
        
        .table-offer { width: 100%; border-collapse: collapse; margin-bottom: 20px; }
        .table-offer th { background: #f8f9fa; text-align: left; padding: 12px; border-bottom: 2px solid var(--primary); }
        .table-offer td { padding: 12px; border-bottom: 1px solid #eee; }
        
        .total-box { margin-left: auto; width: 300px; background: #f8f9fa; padding: 20px; border-radius: 8px; border-left: 5px solid var(--primary); }
        .total-row { display: flex; justify-content: space-between; margin-bottom: 5px; }
        .grand-total { font-size: 14pt; font-weight: bold; color: var(--primary); border-top: 1px solid #ddd; margin-top: 10px; padding-top: 10px; }

        .ins-highlight { background: #fff8e1; border: 1px solid #ffe082; padding: 15px; border-radius: 8px; margin: 20px 0; }
        
        .terms-section { font-size: 8.5pt; color: #777; border-top: 1px solid #eee; padding-top: 20px; margin-top: 40px; column-count: 2; column-gap: 30px; }

        @media print {
            body { background: white; padding: 0; }
            .setup-container, .btn-print-action { display: none !important; }
            #quotationOutput { display: block !important; margin: 0; }
            .a4-quote { box-shadow: none; width: 100%; padding: 15mm; }
        }
    </style>
</head>
<body>

    <div class="setup-container">
        <div class="header-ui">
            <h2 style="margin:0;"><i class="fa-solid fa-file-invoice-dollar"></i> Quotation Offer</h2>
            <img src="https://brothersegy.com/wp-content/uploads/2026/02/12345.png" style="height:40px;">
        </div>

        <div class="grid">
            <div>
                <label>Client Full Name</label>
                <input type="text" id="q_name" placeholder="John Doe">
            </div>
            <div>
                <label>Phone Number</label>
                <input type="text" id="q_phone" placeholder="+20 1XXXXXXXXX">
            </div>
        </div>

        <div class="grid">
            <div>
                <label>Select Vehicle</label>
                <select id="q_car" onchange="updateRate()">
                    <option value="1200">MG 5 (Comfort)</option>
                    <option value="1500">MG ZS (SUV)</option>
                    <option value="1800">Hyundai Tucson</option>
                    <option value="2500">Jetour X90 Plus</option>
                    <option value="1100">Nissan Sunny</option>
                </select>
            </div>
            <div>
                <label>Daily Rate (EGP)</label>
                <input type="number" id="q_rate" value="1200">
            </div>
            <div>
                <label>Duration (Days)</label>
                <input type="number" id="q_days" value="3">
            </div>
        </div>

        <div class="grid">
            <div>
                <label>Insurance Package</label>
                <select id="q_ins">
                    <option value="0">Basic (100% Liability)</option>
                    <option value="200">Intermediate (+200/day)</option>
                    <option value="500">Full Protection (+500/day)</option>
                </select>
            </div>
            <div>
                <label>Security Deposit (EGP)</label>
                <input type="number" id="q_dep" value="5000">
            </div>
        </div>

        <button class="btn-generate" onclick="generateQuote()">Create Professional Offer</button>
    </div>

    <div id="quotationOutput">
        <div class="a4-quote" id="printableQuote">
            <div class="quote-header">
                <img src="https://brothersegy.com/wp-content/uploads/2026/02/12345.png" style="height:60px;">
                <div class="company-meta">
                    <h2 style="color:var(--primary); margin:0;">PRICE QUOTATION</h2>
                    <p>Reference: <span id="out_ref">QT-2702-001</span><br>Date: <span id="out_date">27/02/2026</span></p>
                </div>
            </div>

            <div class="client-bar">
                <div><strong>PREPARED FOR:</strong> <span id="out_name">Client Name</span></div>
                <div><strong>PHONE:</strong> <span id="out_phone">+20...</span></div>
            </div>

            <table class="table-offer">
                <thead>
                    <tr>
                        <th>Service Description</th>
                        <th>Qty</th>
                        <th>Daily Rate</th>
                        <th>Total</th>
                    </tr>
                </thead>
                <tbody id="out_table_body">
                    </tbody>
            </table>

            <div style="display: flex; justify-content: space-between;">
                <div style="width: 50%;">
                    <div class="ins-highlight">
                        <strong style="color:var(--accent);"><i class="fa-solid fa-shield-halved"></i> SELECTED INSURANCE</strong><br>
                        <small id="out_ins_desc">Package details will appear here based on your selection.</small>
                    </div>
                    <p style="font-size: 9pt;">* Valid for 48 hours.<br>* Final availability confirmed upon booking.</p>
                </div>
                <div class="total-box">
                    <div class="total-row"><span>Rental Subtotal:</span> <span id="out_sub">0 EGP</span></div>
                    <div class="total-row"><span>Insurance:</span> <span id="out_ins_total">0 EGP</span></div>
                    <div class="grand-total"><div class="total-row"><span>Grand Total:</span> <span id="out_grand">0 EGP</span></div></div>
                    <div style="margin-top:10px; font-size:10pt; color:var(--accent);"><strong>Security Deposit:</strong> <span id="out_dep">0 EGP</span></div>
                </div>
            </div>

            <div class="terms-section">
                <strong>QUICK TERMS:</strong><br>
                1. Age: 21+ years. 2. License: Valid for 1+ year. 3. KM Limit: 120km/day included. 
                4. Fuel: Return at same level. 5. Extensions: Must be requested 24h in advance.
                6. Cancellation: Free up to 48h before pickup.
                7. Smoking is strictly prohibited inside vehicles.
            </div>

            <div style="margin-top: 50px; display: flex; justify-content: space-between; border-top: 1px solid #eee; padding-top: 20px;">
                <div style="text-align: center;">
                    <p>Brothers EGY Sales Team</p>
                    <div style="height: 40px;"></div>
                    <p>____________________</p>
                </div>
                <div style="text-align: center;">
                    <p>Client Acceptance</p>
                    <div style="height: 40px;"></div>
                    <p>____________________</p>
                </div>
            </div>
        </div>
        <div style="text-align:center; margin-top:20px;">
            <button class="btn-print-action btn-generate" onclick="window.print()" style="width:200px;">Print / Save PDF</button>
        </div>
    </div>

    <script>
        function updateRate() {
            const carSelect = document.getElementById('q_car');
            document.getElementById('q_rate').value = carSelect.value;
        }

        function generateQuote() {
            const name = document.getElementById('q_name').value || "Valued Client";
            const phone = document.getElementById('q_phone').value || "Not Provided";
            const car = document.getElementById('q_car').options[document.getElementById('q_car').selectedIndex].text;
            const rate = parseFloat(document.getElementById('q_rate').value);
            const days = parseInt(document.getElementById('q_days').value);
            const insRate = parseFloat(document.getElementById('q_ins').value);
            const deposit = parseFloat(document.getElementById('q_dep').value);

            // Calculations
            const subtotal = rate * days;
            const insTotal = insRate * days;
            const grandTotal = subtotal + insTotal;

            // Insurance Description
            let insDesc = "";
            const insVal = document.getElementById('q_ins').value;
            if(insVal == "0") insDesc = "Basic Plan: Standard CDW included. Client remains liable for 100% of body damages, glass, and tires.";
            else if(insVal == "200") insDesc = "Intermediate Plan: Reduced liability. 70/30 coverage split on body damages.";
            else insDesc = "Full Protection: Zero deductible. Maximum peace of mind with full coverage on body and mechanicals.";

            // UI Update
            document.getElementById('out_name').innerText = name;
            document.getElementById('out_phone').innerText = phone;
            document.getElementById('out_ref').innerText = "QT-" + Math.floor(1000 + Math.random() * 9000);
            document.getElementById('out_date').innerText = new Date().toLocaleDateString('en-GB');
            
            document.getElementById('out_table_body').innerHTML = `
                <tr>
                    <td><strong>Vehicle Rental:</strong> ${car}</td>
                    <td>${days} Days</td>
                    <td>${rate.toLocaleString()}</td>
                    <td>${subtotal.toLocaleString()} EGP</td>
                </tr>
                ${insRate > 0 ? `<tr><td>Insurance Surcharge</td><td>${days} Days</td><td>${insRate}</td><td>${insTotal.toLocaleString()} EGP</td></tr>` : ''}
            `;

            document.getElementById('out_sub').innerText = subtotal.toLocaleString() + " EGP";
            document.getElementById('out_ins_total').innerText = insTotal.toLocaleString() + " EGP";
            document.getElementById('out_grand').innerText = grandTotal.toLocaleString() + " EGP";
            document.getElementById('out_dep').innerText = deposit.toLocaleString() + " EGP";
            document.getElementById('out_ins_desc').innerText = insDesc;

            document.getElementById('quotationOutput').style.display = 'block';
            window.scrollTo({ top: document.getElementById('quotationOutput').offsetTop, behavior: 'smooth' });
        }
    </script>
</body>
</html>
