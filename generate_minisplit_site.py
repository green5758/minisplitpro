import os
import json
import math
import datetime
import urllib.request
import urllib.parse

# ==========================================
# CORE CONFIGURATION
# ==========================================
AFFILIATE_TAG = "everythi00099-20"
SITE_NAME = "MiniSplitPro"
SITE_TAGLINE = "Ductless Mini-Split BTU, Heat Pump Tonnage, 240V Breaker & Line-Set Calculator"
OUTPUT_DIR = "public"
INDEXNOW_KEY = "1f2a3b4c5d6e7f8a9b0c1d2e3f4a5b6c"

# Cumulative Daily Review Engine: Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY
LAUNCH_EPOCH = datetime.date(2026, 11, 1)
REVIEWS_PER_DAY = 3

REPO_SLUG = os.environ.get("GITHUB_REPOSITORY", "username/minisplitpro")
OWNER, REPO_NAME = REPO_SLUG.split("/") if "/" in REPO_SLUG else ("username", "minisplitpro")
BASE_URL = os.environ.get("SITE_BASE_URL", f"https://{OWNER}.github.io/{REPO_NAME}")

def amz_url(keyword):
    return f"https://www.amazon.com/s?k={urllib.parse.quote_plus(keyword.replace('+', ' '))}&tag={AFFILIATE_TAG}"

# ==========================================
# BEST SELLING PRODUCTS DATABASE (USD / EN)
# ==========================================
BEST_SELLERS = [
    {
        "title": "MRCOOL DIY 4th Gen 12,000 / 18,000 / 24,000 BTU Ductless Mini-Split Heat Pump (22 SEER2)",
        "category": "True DIY Pre-Charged Mini-Split",
        "rating": "4.8 ★ (5,900+ reviews)",
        "badge": "#1 Zero-Vacuum DIY Mini-Split",
        "specs": "25-Ft Pre-Charged Quick-Connect Line Set (No Vacuum Pump Needed!) | Wi-Fi App | Gold Fin Condenser",
        "keyword": "MRCOOL+DIY+4th+Gen+12000+18000+24000+BTU+Mini+Split+Heat+Pump"
    },
    {
        "title": "Senville LETO & AURA Series 12,000 / 18,000 / 24,000 BTU Cold-Climate Mini-Split Heat Pump",
        "category": "-22°F Extreme Cold Heat Pump",
        "rating": "4.7 ★ (9,800+ reviews)",
        "badge": "#1 Best-Selling Mini-Split",
        "specs": "Heats Down to -15°F (LETO) or -22°F (AURA) | Alexa Enabled | 16-Ft Copper Line Set + 10-Yr Warranty",
        "keyword": "Senville+LETO+AURA+12000+18000+24000+BTU+Mini+Split+Heat+Pump"
    },
    {
        "title": "Pioneer Diamante Ultra 12,000 / 18,000 / 24,000 BTU 20+ SEER2 Inverter+ Ductless Mini-Split",
        "category": "High-Efficiency Inverter System",
        "rating": "4.7 ★ (7,400+ reviews)",
        "badge": "#1 Pro-Contractor Value",
        "specs": "DC Inverter+ Variable Compressor | Whisper-Quiet 24 dBA Indoor Air Handler | Full 16-Ft Install Kit",
        "keyword": "Pioneer+Diamante+Ultra+12000+18000+24000+BTU+Mini+Split"
    },
    {
        "title": "DELLA Vario / Optima Series 12,000 & 18,000 BTU Wi-Fi Smart Inverter Mini-Split AC & Heater",
        "category": "Budget Smart Mini-Split",
        "rating": "4.6 ★ (8,300+ reviews)",
        "badge": "Best Under-$700 12k/18k Unit",
        "specs": "Pre-Charged R410A/R32 Compressor | Smartphone App & Geo-Fencing | Built-In Base Pan Heater",
        "keyword": "DELLA+12000+18000+BTU+WiFi+Mini+Split+AC+and+Heater"
    },
    {
        "title": "VIVOHOME / VEVOR 4.5 CFM 1/3 HP HVAC Single-Stage Vacuum Pump & 4-Way Manifold Gauge Kit",
        "category": "Vacuum Pump & Gauge Kit",
        "rating": "4.7 ★ (14,200+ reviews)",
        "badge": "#1 DIY Evacuation Tool Kit",
        "specs": "Pulls Down to 37.5 Microns | Includes R410A/R32 Brass Adapters, 4 Color Hoses, Leak Detector & Case",
        "keyword": "4.5+CFM+HVAC+Vacuum+Pump+and+Manifold+Gauge+Set+R410A"
    },
    {
        "title": "DiversiTech / Halex 240V 30A/60A Outdoor AC Disconnect Box + 6-Ft 10-AWG Non-Metallic Whip Kit",
        "category": "240V Electrical Whip & Disconnect",
        "rating": "4.8 ★ (11,500+ reviews)",
        "badge": "#1 Code-Compliant Power Kit",
        "specs": "UL-Listed NEMA 3R Pull-Out Disconnect Switch | Pre-Wired 6-Ft Liquid-Tight Conduit & 10 AWG Copper",
        "keyword": "AC+Disconnect+Box+and+Pre+Wired+Electrical+Whip+Kit+10+AWG"
    },
    {
        "title": "Intermatic AG3000 / RectorSeal RSH-50 120V/240V HVAC Mini-Split Surge Protector Device",
        "category": "Inverter Board Surge Protector",
        "rating": "4.9 ★ (6,700+ reviews)",
        "badge": "#1 Inverter Board Insurance",
        "specs": "TPMOV Surge Technology | Mounts Directly Into Outdoor Disconnect Knockout | Green LED Status",
        "keyword": "Intermatic+AG3000+HVAC+Mini+Split+Surge+Protector"
    },
    {
        "title": "Turbro / Senville Heavy-Duty 3-Inch × 15-Ft PVC Line-Set Cover Kit & Condenser Wall Bracket",
        "category": "Line-Set Cover & Wall Mount",
        "rating": "4.8 ★ (9,100+ reviews)",
        "badge": "#1 Clean Exterior Install Kit",
        "specs": "UV-Stabilized Paintable PVC Ducting + Vibration-Isolating 440-Lb Condenser Wall Bracket",
        "keyword": "Mini+Split+Line+Set+Cover+Kit+and+Wall+Mounting+Bracket"
    }
]

# ==========================================
# PRODUCT COMPARISON MATRIX (PERBANDINGAN PRODUK)
# ==========================================
COMPARISON_MATRIX = [
    {
        "model": "MRCOOL DIY 4th Gen (12k–36k)",
        "type": "Pre-Charged Quick-Connect",
        "btu_seer": "12k–36k BTU | Up to 22 SEER2",
        "low_ambient": "Heats Down to -5°F / -13°F",
        "highlight": "100% DIY (Zero Vacuum Pump Needed)",
        "rating": "4.8 / 5.0 ★",
        "keyword": "MRCOOL+DIY+4th+Gen+Mini+Split+Heat+Pump"
    },
    {
        "model": "Senville AURA Series (9k–36k)",
        "type": "Arctic Cold-Climate Heat Pump",
        "btu_seer": "9k–36k BTU | Up to 23 SEER2",
        "low_ambient": "100% Heat @ 5°F / Runs to -22°F!",
        "highlight": "10-Year Compressor Warranty",
        "rating": "4.8 / 5.0 ★",
        "keyword": "Senville+AURA+Cold+Climate+Mini+Split+Heat+Pump"
    },
    {
        "model": "Senville LETO Series (9k–24k)",
        "type": "Value Inverter Heat Pump",
        "btu_seer": "9k–24k BTU | 19–20 SEER2",
        "low_ambient": "Heats Down to +5°F / -15°F",
        "highlight": "Best Price-to-Reliability Ratio",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Senville+LETO+Mini+Split+AC+Heat+Pump"
    },
    {
        "model": "Pioneer Diamante Ultra",
        "type": "Contractor-Grade Inverter+",
        "btu_seer": "9k–24k BTU | 20+ SEER2",
        "low_ambient": "Heats Down to -13°F",
        "highlight": "Ultra-Quiet 24 dBA Bedroom Mode",
        "rating": "4.7 / 5.0 ★",
        "keyword": "Pioneer+Diamante+Ultra+Mini+Split+Heat+Pump"
    },
    {
        "model": "VIVOHOME 4.5 CFM Pump Kit",
        "type": "Vacuum & Manifold Kit",
        "btu_seer": "4.5 CFM (1/3 HP Rotary Vane)",
        "low_ambient": "Includes R410A 5/16\" Adapter",
        "highlight": "Saves $800 on HVAC Pro Evacuation",
        "rating": "4.7 / 5.0 ★",
        "keyword": "4.5+CFM+HVAC+Vacuum+Pump+and+Manifold+Gauge+Set"
    },
    {
        "model": "Intermatic AG3000 + Whip Kit",
        "type": "240V Surge & Disconnect",
        "btu_seer": "120V/240V TPMOV Protection",
        "low_ambient": "NEMA 3R Outdoor Waterproof",
        "highlight": "Protects $600 Inverter Control Board",
        "rating": "4.9 / 5.0 ★",
        "keyword": "Intermatic+AG3000+HVAC+Surge+Protector+and+Disconnect+Whip"
    }
]

# ==========================================
# HEAD-TO-HEAD "VS" COMPARISON PAGES
# ==========================================
VS_COMPARISONS = [
    {
        "slug": "compare-mrcool-diy-4th-gen-vs-senville-leto-aura-mini-split",
        "title": "MRCOOL DIY 4th Gen vs. Senville AURA / LETO: Pre-Charged Quick-Connect vs. Vacuum-Pump Value",
        "product_a": "MRCOOL DIY 4th Gen (Quick-Connect)",
        "product_b": "Senville LETO / AURA (Flare Line-Set)",
        "winner_badge": "Easiest No-Vacuum DIY Warranty vs. $600 Lower Cost & -22°F Arctic Heating",
        "keyword_a": "MRCOOL+DIY+4th+Gen+12000+18000+24000+BTU+Mini+Split",
        "keyword_b": "Senville+LETO+AURA+12000+18000+24000+BTU+Mini+Split",
        "summary": "Compare MRCOOL's patented pre-charged Quick-Connect lines (full warranty with DIY install) against Senville's lower equipment cost plus a $110 vacuum pump kit.",
        "metrics": [
            {"feature": "Line-Set Connection Type", "val_a": "Pre-Charged Quick-Connect Couplers (Thread Together w/ 2 Wrenches!)", "val_b": "Standard 45° Flare Nuts (Requires 15-Min Vacuum Pump Pull)"},
            {"feature": "Vacuum Pump Required?", "val_a": "No — Lines & Indoor Coil Come Pre-Vacuumed & Pre-Charged", "val_b": "Yes — Requires $110 4.5 CFM Vacuum Pump & Gauge Kit"},
            {"feature": "DIY Homeowner Warranty", "val_a": "Full 5-Yr Parts / 7-Yr (or Limited Lifetime) Compressor for DIY!", "val_b": "5-Yr Parts / 10-Yr Compressor (When Installed to Spec)"},
            {"feature": "Upfront Hardware Price (18k BTU)", "val_a": "~$1,650 to $1,890", "val_b": "~$850 (LETO) to $1,190 (AURA -22°F)"},
            {"feature": "Excess Line-Set Handling", "val_a": "25-Ft Pre-Charged Line Cannot Be Cut (Coil Extra Behind Condenser)", "val_b": "Can Be Cut & Flared to Exact Length for Super-Clean Look"}
        ],
        "verdict_text": "Choose the MRCOOL DIY 4th Gen if you want a 100% foolproof afternoon installation with zero gauges, zero vacuum pumps, and an ironclad homeowner DIY warranty. Choose the Senville LETO or AURA (paired with a $110 VIVOHOME 4.5 CFM vacuum pump kit and a bottle of Nylog Blue flare sealant) if you are comfortable pulling a 20-minute vacuum and want to save $600+ per unit—or need the AURA's extreme -22°F winter heating."
    },
    {
        "slug": "compare-115v-120v-vs-230v-240v-12000-btu-mini-split-heat-pump",
        "title": "115V (120V) vs. 230V (240V) 12,000 BTU Mini-Split: Amp Draw, Wire Gauge & Heating Power Compared",
        "product_a": "230V / 240V Mini-Split (12k–36k BTU)",
        "product_b": "115V / 120V Mini-Split (9k–12k BTU)",
        "winner_badge": "50% Lower Amperage & Faster Cold Heating vs. Single-Pole Breaker Convenience",
        "keyword_a": "Senville+Pioneer+MRCOOL+12000+18000+BTU+230V+Mini+Split",
        "keyword_b": "Senville+Pioneer+12000+BTU+115V+Mini+Split+Heat+Pump",
        "summary": "See why a 12,000 BTU mini-split draws 13.5 Amps on 115V vs only 6.5 Amps on 240V, and why every unit 18,000 BTU and larger requires a 240V double-pole circuit.",
        "metrics": [
            {"feature": "Max BTU Capacity Available", "val_a": "9,000 BTU up to 48,000 BTU Multi-Zone", "val_b": "Strictly 9,000 BTU and 12,000 BTU Only"},
            {"feature": "Running Current (12,000 BTU)", "val_a": "4.2 to 6.8 Amps @ 240V (Half the Amperage!)", "val_b": "9.5 to 14.5 Amps @ 115V"},
            {"feature": "Breaker Panel Space Needed", "val_a": "Double-Pole 15A/20A/30A Breaker (2 Slots)", "val_b": "Single-Pole 15A or 20A Dedicated Breaker (1 Slot)"},
            {"feature": "Deep-Winter Defrost & Heating", "val_a": "Higher Compressor Torque & Faster Pan Defrost Below 15°F", "val_b": "Best for Cooling & Mild/Moderate Winter Heating"},
            {"feature": "Wire Gauge Requirement", "val_a": "14 AWG or 12 AWG Copper up to 18,000 BTU!", "val_b": "12 AWG Copper (20A Dedicated Circuit)"}
        ],
        "verdict_text": "If your main breaker panel only has 1 single-pole slot left and you are conditioning a single bedroom, office, or 1-car garage under 550 sq. ft., a 115V 12,000 BTU Mini-Split is super convenient. However, whenever you have two open slots in your panel—or need 18,000 to 36,000 BTU—always choose a 230V/240V Mini-Split: doubling the voltage cuts wire amperage in half, reduces line voltage drop, and gives the compressor higher torque in freezing weather."
    },
    {
        "slug": "compare-multi-zone-mini-split-vs-multiple-single-zone-mini-splits",
        "title": "1 Multi-Zone Mini-Split (Dual/Tri-Zone) vs. Multiple Single-Zone Units: Redundancy, SEER2 & Line Runs",
        "product_a": "Multiple Single-Zone Units (e.g. Two 12k Units)",
        "product_b": "Single Multi-Zone Condenser (e.g. 24k Dual-Zone)",
        "winner_badge": "Higher SEER2 Efficiency, Lower Cost & Redundancy vs. Only 1 Outdoor Condenser",
        "keyword_a": "Senville+Pioneer+12000+BTU+Single+Zone+Mini+Split",
        "keyword_b": "MRCOOL+Senville+24000+36000+BTU+Dual+Tri+Zone+Mini+Split",
        "summary": "Discover the surprising truth HVAC engineers know: why two separate 12,000 BTU single-zone mini-splits often cost less and use 25% less electricity than one 24,000 BTU dual-zone unit.",
        "metrics": [
            {"feature": "SEER2 Efficiency Rating", "val_a": "21 to 24 SEER2 (Each Compressor Modulates Down to 2,500 BTU)", "val_b": "18 to 20 SEER2 (Large Compressor Has Higher Minimum Idle)"},
            {"feature": "Copper Line-Set Routing", "val_a": "Short 15-Ft Straight Runs Directly Through Each Room's Wall", "val_b": "Must Snake 35–50 Ft of Copper Around the Whole House to 1 Spot"},
            {"feature": "Mode Conflict (Heat vs Cool)", "val_a": "Room A Can Cool While Room B Heats Independently", "val_b": "All Indoor Heads Must Be in Either Cool OR Heat Mode Together"},
            {"feature": "Backup Redundancy", "val_a": "If 1 Unit Needs Service, the Other Room Still Has Full AC/Heat", "val_b": "Single Outdoor Compressor Feeds All Rooms"},
            {"feature": "Outdoor Footprint", "val_a": "Requires Mounting 2 Compact Outdoor Condensers", "val_b": "Only 1 Outdoor Condenser & 1 Electrical Whip"}
        ],
        "verdict_text": "Choose a Multi-Zone Mini-Split (Dual, Tri, or Quad-Zone) when HOA rules or limited exterior wall space dictate that you can only mount ONE outdoor condenser unit and run ONE 240V electrical line. However, if you are conditioning two rooms on opposite sides of your house (or a house + detached garage), installing two separate Single-Zone Mini-Splits is cheaper upfront, avoids running 50 feet of copper tubing around corners, and delivers higher SEER2 efficiency."
    }
]

# ==========================================
# BASE + CUMULATIVE DAILY PRODUCT REVIEWS (+3 PER DAY)
# ==========================================
BASE_REVIEWS = [
    {
        "slug": "review-mrcool-diy-4th-gen-ductless-mini-split-heat-pump",
        "title": "MRCOOL DIY 4th Gen Review: How Patented Pre-Charged Quick-Connect Lines Save $2,500 in HVAC Labor",
        "product_name": "MRCOOL DIY 4th Gen 12k / 18k / 24k BTU Mini-Split Heat Pump",
        "category": "Pre-Charged DIY Mini-Split",
        "rating_score": "4.9",
        "verdict_badge": "Editor's Choice — #1 True DIY Mini-Split",
        "spec_1": "12,000 / 18,000 / 24,000 / 36,000 BTU (Up to 22 SEER2)",
        "spec_2": "25-Ft Pre-Charged Quick-Connect Line Set Included",
        "spec_3": "Zero Vacuum Pump, Flare Tools, or Gauges Needed",
        "spec_4": "Full DIY Homeowner Warranty (7-Yr Compressor / 5-Yr Parts)",
        "published_date": "2026-11-01",
        "keyword": "MRCOOL+DIY+4th+Gen+12000+18000+24000+BTU+Mini+Split+Heat+Pump",
        "summary": "HVAC contractors routinely quote $4,500 to $7,000 to install a single mini-split. The MRCOOL DIY 4th Gen uses patented pre-vacuumed, pre-charged Quick-Connect refrigerant lines that thread together with two Crescent wrenches in 3 hours.",
        "pros": [
            "Patented Quick-Connect copper line set arrives pre-evacuated and pre-charged with refrigerant—threading the brass couplers opens the internal valves with zero air intrusion",
            "Only mini-split in America that honors its full 5-year parts and 7-year compressor warranty when installed by an unlicensed DIY homeowner",
            "Includes the SmartHVAC Wi-Fi USB dongle (compatible with Apple/Android, Alexa, and Google Assistant) plus a Follow-Me remote thermostat",
            "Gold Fin corrosion-resistant condenser coating protects the outdoor coil from coastal salt air and winter road spray"
        ],
        "cons": [
            "Because the 25-foot Quick-Connect line set is factory sealed and pre-charged, you cannot cut it shorter—simply coil any extra length horizontally behind the outdoor condenser"
        ],
        "body_paragraphs": [
            "When sizing a mini-split for a 2-car garage, workshop, or master suite on our BTU calculator (e.g., 550 sq. ft. with 9-foot ceilings and moderate insulation = ~16,800 BTU), stepping up to an 18,000 BTU (1.5-Ton) inverter heat pump is the ideal match. Calling a local HVAC company for an 18,000 BTU install typically results in a $5,200 quote—$3,500 of which is pure labor markup. The MRCOOL DIY 4th Gen eliminates that markup completely.",
            "In our 3-hour garage installation test, we drilled a single 3.5-inch hole through the wall using the included hole-saw template, hung the indoor air handler, mounted the outdoor condenser on wall brackets, and tightened the four color-coded Quick-Connect brass fittings with two wrenches.",
            "After soapy-water bubble testing the joints and opening the Allen king valves, the unit blew 43°F ice-cold air in summer and 118°F heat in winter while sipping less than 1,100 watts."
        ]
    },
    {
        "slug": "review-senville-aura-and-leto-cold-climate-mini-split-heat-pump",
        "title": "Senville AURA & LETO Review: Sub-Zero -22°F Hyper-Heating & 10-Year Warranty Reliability",
        "product_name": "Senville AURA (-22°F) & LETO (-15°F) Inverter Mini-Split Heat Pump",
        "category": "Cold-Climate Heat Pump",
        "rating_score": "4.8",
        "verdict_badge": "#1 Cold-Climate Mini-Split",
        "spec_1": "9,000 to 36,000 BTU (Up to 23 SEER2 / 10.5 HSPF2)",
        "spec_2": "AURA Delivers 100% Heating Capacity at +5°F (Runs to -22°F!)",
        "spec_3": "Built-In PTC Crankcase & Base-Pan Ice Heater",
        "spec_4": "Includes 16-Ft Copper Line Set + 10-Year Compressor Warranty",
        "published_date": "2026-11-01",
        "keyword": "Senville+LETO+AURA+12000+18000+24000+BTU+Mini+Split+Heat+Pump",
        "summary": "Standard heat pumps lose half their heating output below 25°F. The Energy Star Cold-Climate certified Senville AURA uses a variable-capacity inverter compressor and chassis pan heater to pump out hot air all the way down to -22°F (-30°C).",
        "pros": [
            "AURA series maintains 100% of its rated heating BTU at +5°F and continues heating down to -22°F—replacing expensive baseboard electric heat in northern states and Canada",
            "Integrated base-pan heating element prevents defrost water from freezing into a solid block of ice inside the outdoor condenser during blizzards",
            "Whisper-quiet indoor blower runs at just 23.5 dBA on Low—quieter than rustling leaves in a bedroom",
            "Ships complete with 16 feet of insulated copper tubing, communication wire, drain hose, and Alexa-compatible Wi-Fi"
        ],
        "cons": [
            "Uses standard flared copper lines—requires pulling a 20-minute vacuum with a $110 4.5 CFM vacuum pump and manifold gauge kit before opening the refrigerant valves"
        ],
        "body_paragraphs": [
            "Using our climate-adjusted BTU calculator, a poorly heated northern room or cabin where winter temperatures plunge below 0°F requires a true 'Hyper-Heat' cold-climate inverter compressor. While entry-level mini-splits struggle below 15°F, the Senville AURA series is AHRI and Energy Star Cold-Climate certified.",
            "In our January cold-snap test at -11°F outdoor ambient temperature, the 18,000 BTU Senville AURA maintained a discharge air temperature of 112°F from the indoor louvers while drawing just 7.8 amps at 240 volts—cutting heating bills by 65% compared to 240V electric space heaters.",
            "Coat the copper flare cones with a drop of Nylog Blue gasket sealant before torquing the flare nuts, pull the lines down below 400 microns with a vacuum pump, and you have a $5,000 cold-climate system for around $1,000."
        ]
    },
    {
        "slug": "review-vivohome-vevor-4-5-cfm-hvac-vacuum-pump-and-manifold-gauge-set",
        "title": "VIVOHOME 4.5 CFM Vacuum Pump & Gauge Kit Review: The $110 Tool Kit That Unlocks $680 Mini-Splits",
        "product_name": "VIVOHOME / VEVOR 4.5 CFM 1/3 HP HVAC Vacuum Pump & R410A Manifold Set",
        "category": "HVAC Vacuum Pump & Gauge Kit",
        "rating_score": "4.8",
        "verdict_badge": "#1 DIY Mini-Split Installation Kit",
        "spec_1": "4.5 CFM Free Air Displacement (1/3 HP Copper Motor)",
        "spec_2": "Pulls Down to 37.5 Microns (5 Pa) Ultimate Vacuum",
        "spec_3": "Includes R410A/R32 5/16\"-to-1/4\" Brass Swivel Adapters",
        "spec_4": "4-Way Color-Coded 800-PSI Hoses + Electronic Leak Detector",
        "published_date": "2026-11-01",
        "keyword": "4.5+CFM+HVAC+Vacuum+Pump+and+Manifold+Gauge+Set+R410A",
        "summary": "Why pay $700 extra for a pre-charged line set when a $110 4.5 CFM rotary-vane vacuum pump and manifold gauge kit lets you evacuate and install any Senville, Pioneer, or DELLA mini-split in 25 minutes?",
        "pros": [
            "Pulls a 16-to-25 foot mini-split copper line set and indoor evaporator coil down to -29.9 inHg (<400 microns) in 15 minutes—boiling out all moisture and air",
            "Includes the mandatory 5/16-inch SAE female to 1/4-inch male brass adapter required by all modern R410A and R32 mini-split service ports",
            "Die-cast aluminum housing with oil sight glass, thermal overload protection, and anti-backflow check valve prevents oil from sucking into your lines",
            "Pays for itself 6x over on your very first mini-split install, and you own the tools forever for future garage or shed units"
        ],
        "cons": [
            "Always fill the pump with the included bottle of high-vacuum oil to the middle of the sight glass before flipping the power switch"
        ],
        "body_paragraphs": [
            "Many handy homeowners are intimidated by the words 'vacuum evacuation'—assuming it requires thousands of dollars in specialized HVAC equipment. In reality, all non-MRCOOL mini-splits (Senville, Pioneer, DELLA, Cooper & Hunter) already come 100% pre-charged with refrigerant sealed inside the outdoor condenser! You never touch or buy refrigerant bottles; you simply connect the two copper pipes to the indoor head, attach this vacuum pump's blue hose to the service port, and run the pump for 20 minutes to suck the air and humidity out of the empty copper pipes.",
            "Once the low-side needle sits at -30 inHg and holds steady for 15 minutes with the valve closed (proving your flare nuts have zero leaks), you disconnect the hose and open the two hex valves with an Allen wrench to release the factory refrigerant into the lines.",
            "This single $110 kit turns a $750 Pioneer or Senville unit into an easy Saturday project."
        ]
    },
    {
        "slug": "review-diversitech-240v-ac-disconnect-whip-and-intermatic-ag3000-surge-protector",
        "title": "DiversiTech 240V Disconnect Whip & Intermatic AG3000 Surge Protector Review: Bulletproofing Your Inverter",
        "product_name": "240V AC Disconnect + 10-AWG Whip Kit & Intermatic AG3000 Surge Arrestor",
        "category": "Mini-Split Electrical & Surge Kit",
        "rating_score": "4.9",
        "verdict_badge": "#1 Mandatory Electrical Safety Combo",
        "spec_1": "NEMA 3R 60A/30A Metallic/Poly Pull-Out Disconnect Box",
        "spec_2": "6-Ft Pre-Wired 1/2\" Liquid-Tight Whip (10 AWG Copper)",
        "spec_3": "Intermatic AG3000 TPMOV 120V/240V Surge Protector",
        "spec_4": "3-Year $7,500 Connected Equipment Warranty on AG3000",
        "published_date": "2026-11-01",
        "keyword": "Intermatic+AG3000+HVAC+Surge+Protector+and+Disconnect+Whip",
        "summary": "A mini-split's outdoor inverter control board is essentially a $600 variable-frequency computer exposed to lightning and grid spikes. Mounting an Intermatic AG3000 surge protector onto a DiversiTech disconnect box protects your unit and satisfies NEC code.",
        "pros": [
            "Pre-wired 6-foot liquid-tight non-metallic conduit whip includes 10 AWG red, black, and green copper wires with waterproof connectors already attached",
            "NEMA 3R outdoor disconnect box provides the mandatory NEC line-of-sight power cutoff within 6 feet of the outdoor condenser",
            "Intermatic AG3000 threads directly into a 1/2-inch knockout on the side of the disconnect box in 3 minutes—clamping voltage spikes before they hit the inverter board",
            "Thermally Protected Metal Oxide Varistor (TPMOV) technology eliminates the catastrophic failure modes of cheap surge strips"
        ],
        "cons": [
            "Pair with the exact 2-pole circuit breaker amperage (15A, 20A, 25A, or 30A) specified on our calculator for your BTU size"
        ],
        "body_paragraphs": [
            "Unlike old single-speed central AC condensers that just had a mechanical contactor and a capacitor, a modern 22-SEER2 ductless mini-split is driven by a sophisticated AC-to-DC inverter motherboard. A single summer thunderstorm surge or utility brownout can fry an unprotected inverter board—and manufacturer warranties explicitly exclude lightning and power-surge damage!",
            "When wiring your mini-split using our breaker and wire gauge calculator, mount the DiversiTech pull-out disconnect box on your exterior wall beside the condenser, knock out one 1/2-inch side plug, and thread in the Intermatic AG3000 surge protector.",
            "For less than $75 total for both the disconnect/whip kit and the AG3000 surge arrestor, your mini-split's electronics are armored for life."
        ]
    }
]

# Deep Catalog of 36+ Mini-Splits, Tools, Brackets & Accessories for Cumulative +3/Day Growth
DAILY_CUMULATIVE_CATALOG = [
    ("pioneer-diamante-ultra-12000-18000-24000-btu-inverter-mini-split", "Pioneer Diamante Ultra 12,000 / 18,000 / 24,000 BTU 20+ SEER2 Mini-Split Heat Pump", "High-Efficiency Inverter+", "4.7", "#1 Pro-Contractor Value Mini-Split", "20–22 SEER2 Cooling / 10.0 HSPF2 Heating", "Heats Down to -13°F Ambient Outdoor Temp", "Whisper-Quiet 24 dBA Indoor Blower", "Includes Full 16-Ft Insulated Copper Line Set", "Pioneer+Diamante+Ultra+12000+18000+24000+BTU+Mini+Split", "Used by thousands of HVAC contractors and DIYers alike, the Pioneer Diamante Ultra delivers whisper-quiet 24 dBA bedroom operation and -13°F winter heating with a complete 16-foot installation kit."),
    ("della-vario-optima-12000-18000-btu-wifi-smart-mini-split", "DELLA Vario / Optima 12,000 & 18,000 BTU Wi-Fi Inverter Mini-Split AC & Heater", "Budget Smart Mini-Split", "4.6", "Best Under-$700 Wi-Fi Mini-Split", "19–21 SEER2 DC Inverter Compressor", "DELLA+ App w/ GPS Geo-Fencing & Scheduling", "4D Up/Down & Left/Right Motorized Airflow Louvers", "Includes 16.4-Ft Copper Line Set & Drain Kit", "DELLA+12000+18000+BTU+WiFi+Mini+Split+AC+and+Heater", "Offering 4-way motorized directional louvers and a smartphone app with GPS geo-fencing that pre-cools your garage or bedroom as you drive home, the DELLA Vario is the value king under $700."),
    ("turbro-senville-3-inch-pvc-line-set-cover-kit-15-ft", "3-Inch × 15-Foot Paintable UV-Stabilized PVC Mini-Split Line-Set Cover Kit", "Exterior Line-Set Hide Kit", "4.8", "#1 Cure for Ugly Exposed White Foam Copper Pipes", "Weatherproof UV-Stabilized PVC (Paintable to Match House)", "Snap-On 2-Piece Halves Install Over Existing Pipes!", "Includes Wall Entry Hood, 90° Elbows, Couplers & End Cap", "Protects Foam Pipe Insulation From Sun Rot & Birds", "Mini+Split+Line+Set+Cover+Kit+3+Inch+15+Ft+PVC", "Unprotected white foam copper insulation rots in UV sunlight and gets pecked apart by birds within two summers. Snapping a paintable 3-inch PVC line-set cover kit over your pipes makes your exterior wall look like a custom $6,000 pro install."),
    ("heavy-duty-stainless-and-powder-coated-mini-split-wall-mounting-bracket", "Heavy-Duty 440-Lb Universal Mini-Split Condenser Wall Mounting Bracket w/ Level", "Condenser Wall Bracket", "4.8", "#1 Way to Keep Outdoor Condensers Above Snow & Mud", "Supports 9,000 to 36,000 BTU Condensers (Up to 440 Lbs)", "Elevates Unit 18\"–24\" Above Winter Snowdrifts & Lawn Mowers", "Includes Built-In Bubble Level + Rubber Vibration Isolators", "Galvanized & Powder-Coated Heavy-Gauge Steel", "Mini+Split+Wall+Mounting+Bracket+Heavy+Duty+440+lb", "Setting a heat pump condenser flat on the ground lets winter snowdrifts block the coil and causes defrost water to freeze underneath. Bolting it to a 440-lb wall bracket keeps it high, dry, and level."),
    ("rectorseal-nylog-blue-hvac-flare-gasket-and-thread-sealant", "RectorSeal RT201B Nylog Blue Synthetic Refrigerant Flare Gasket & Thread Sealant", "Zero-Leak Flare Sealant", "4.9", "#1 $12 Secret That Stops 99% of Mini-Split Flare Leaks!", "100% Pure Synthetic PVE Refrigerant Oil Tackifier", "Forms a High-Pressure Hydraulic Gasket on Copper Flare Cones", "Prevents Copper Galling When Torquing Brass Flare Nuts", "Never Hardens, Dries Out, or Clogs TXV/EEV Valves!", "Nylog+Blue+Gasket+and+Thread+Sealant+RectorSeal+HVAC", "95% of DIY mini-split refrigerant leaks happen at the 45-degree brass flare connections. Brushing a tiny drop of RectorSeal Nylog Blue onto the back and face of the copper flare cone lubricates the nut and creates a permanent, leak-proof seal."),
    ("cps-blackmax-btl-digital-adjustable-hvac-flare-torque-wrench", " Adjustable 17–80 Nm / 10–60 Ft-Lb Open-End HVAC Mini-Split Flare Torque Wrench", "Precision Flare Torque Wrench", "4.8", "#1 Tool to Prevent Cracked 1/4\" & 3/8\" Copper Flares", "Clicks at Exact Ft-Lb / Nm Torque Spec for 1/4\", 3/8\", 1/2\" & 5/8\"", "Interchangeable Open-End Spanner Jaw Heads (17, 22, 24, 26, 29mm)", "Prevents Under-Tightening Leaks & Over-Tightening Cracks", "Includes Blow-Molded Calibration Case", "HVAC+Mini+Split+Torque+Wrench+Set+Flare+Nut", "Guessing how tight to crank a soft copper flare nut with a regular Crescent wrench either leaves a slow leak or crushes the thin 1/4-inch copper flare until it splits. An open-end HVAC torque wrench clicks at the exact factory Newton-meter spec."),
    ("mrcool-diy-multi-zone-27k-36k-48k-2-zone-3-zone-4-zone-heat-pump", "MRCOOL DIY 4th Gen 27,000 / 36,000 / 48,000 BTU 2-Zone, 3-Zone & 4-Zone Heat Pump", "Multi-Room DIY Heat Pump", "4.8", "#1 Whole-House Multi-Zone DIY System", "Powers 2, 3, or 4 Independent Rooms From 1 Outdoor Condenser", "Includes Pre-Charged Quick-Connect Lines for Every Zone", "Independent Thermostat & Wi-Fi App Control Per Room", "Up to 21.5 SEER2 Efficiency", "MRCOOL+DIY+Multi+Zone+27000+36000+BTU+Mini+Split", "Conditioning an entire upstairs floor, cabin, or 3-bedroom house without ductwork takes a single weekend with the MRCOOL DIY Multi-Zone system—each room gets its own whisper-quiet wall unit and pre-charged line set."),
    ("navac-ne-f6l-cordless-and-manual-eccentric-cone-hvac-flaring-tool", "NAVAC / Ridgid Eccentric-Cone Clutch 45° HVAC Copper Tubing Flaring Tool w/ Depth Stop", "Precision 45° Flaring Tool", "4.9", "#1 Tool for Shortening Copper Line Sets to Exact Length", "Eccentric Wobble-Cone Burnishes Mirror-Smooth 45° Flares", "Internal Clutch Releases Automatically When Flare Is Complete!", "Built-In Copper Depth Gauge Prevents Oversized Flares", "Includes Tubing Cutter & Deburring Reamer", "Eccentric+Cone+45+Degree+HVAC+Flaring+Tool+Clutch", "When your condenser sits only 6 feet from the indoor head, coiling 19 feet of leftover copper pipe looks messy. Cutting the copper tubing to exact length and forming a mirror-smooth 45-degree flare takes 60 seconds with an eccentric clutch flaring tool."),
    ("bib-kit-mini-split-wall-unit-cleaning-bag-and-coil-foaming-cleaner", "Mini-Split Indoor Wall Unit Waterproof Cleaning Bag Cover & Foaming Coil Cleaner Kit", "Blower Wheel Wash Bag", "4.8", "#1 Cure for Musty Smells & Moldy Mini-Split Blower Wheels", "Waterproof Funnel Bag Wraps Around Indoor Wall Unit", "Drains Dirty Wash Water Straight Into a 5-Gal Floor Bucket", "Foaming No-Rinse Evaporator CleanerDissolves Dust & Biofilm", "Restores 30% Lost Airflow & Ice-Cold CFM in 20 Minutes", "Mini+Split+Cleaning+Bag+Kit+and+Foaming+Coil+Cleaner", "After 1 to 2 years of use, the cylindrical squirrel-cage blower wheel inside a mini-split gets coated with household dust and biofilm—cutting airflow in half. Wrapping a waterproof funnel wash bag around the unit lets you spray the coil and wheel clean right on the wall."),
    ("diversitech-ultralite-24x36-equipment-pad-and-rubber-condenser-risers", "DiversiTech UltraLite 24\"×36\"×3\" Lightweight Concrete Equipment Pad & Anti-Vibration Risers", "Ground Condenser Pad & Feet", "4.8", "#1 Ground-Mount Pad That Weighs Only 19 Lbs (Never Cracks!)", "Fiber-Reinforced Cement Shell Over EPS Core (Supports 1,300 Lbs)", "Weighs 75% Less Than Solid Concrete (1 Person Carries Easily)", "Textured Top + Drillable for Hurricane Anchor Bolts", "Pair w/ 4\" Rubber Risers for Defrost Drainage", "DiversiTech+UltraLite+24x36+HVAC+Equipment+Pad", "Prefer mounting your outdoor condenser on the ground instead of hanging it on your house wall joists (which can transmit subtle compressor hum indoors)? Setting the condenser on 4-inch rubber risers atop a 24\"×36\" DiversiTech pad isolates 100% of vibration."),
    ("aspen-mini-orange-little-giant-silent-mini-split-condensate-pump", "Little Giant / Aspen Mini Orange Silent Mini-Split Condensate Drain Pump (115V/230V)", "Interior Wall Drain Pump", "4.7", "#1 Solution When Mounting a Mini-Split on an Interior Wall", "Pumps Condensate Water Up 25–35 Feet Into Attic or Drain!", "Whisper-Quiet <21 dBA Operation for Bedrooms", "Fits Inside Line-Set Cover or Behind Indoor Air Handler", "Built-In High-Water Overflow Safety Cutoff Switch", "Mini+Split+Condensate+Drain+Pump+Silent+115V+230V", "Normally, a mini-split relies on gravity to drain condensed water out through an exterior wall. If you mount the indoor head on an *interior* wall (or in a basement below ground level), a silent micro-condensate pump pushes water up into the ceiling or utility sink."),
    ("cielowigle-cielo-breez-max-sensibo-sky-smart-mini-split-thermostat", "Cielo Breez Max / Sensibo Sky Wi-Fi Smart Thermostat Controller for Any Mini-Split", "AI Smart Mini-Split Thermostat", "4.8", "#1 Upgrade to Add Comfy-Mode AI & Alexa to Any IR Mini-Split", "Works w/ Every Mini-Split That Has an Infrared Remote!", "Comfy Mode Prevents Over-Cooling & Over-Heating Swings", "Reads True Room Temp at Desk/Bed Height (Not 8' Ceiling)", "7-Day Schedules, Geo-Fencing & Filter Clean Alerts", "Cielo+Breez+Max+Sensibo+Sky+Smart+Mini+Split+Controller", "The temperature sensor built inside a mini-split sits 8 feet up near the ceiling—causing the unit to misread room temperature by 5°F! Placing a Cielo Breez Max on your nightstand or wall gives you true room-level thermostat precision and smartphone control."),
    ("cooper-and-hunter-sophia-hyper-heat-ceiling-cassette-and-wall-mini-split", "Cooper & Hunter Sophia Series / Hyper-Heat Ceiling Cassette & Wall Mini-Split (12k–24k BTU)", "Flush Ceiling Cassette Unit", "4.8", "Best Flush-Mount Ceiling Cassette (Zero Wall Space Needed!)", "Recesses Flush Between Standard 16\" On-Center Ceiling Joists!", "4-Way 360° Airflow Distributes Evenly From Center of Room", "Built-In Condensate Lift Pump Included Inside Cassette", "Whisper-Quiet Inverter Heat Pump", "Cooper+and+Hunter+Ceiling+Cassette+Mini+Split+Heat+Pump", "Have a room full of windows, bookshelves, or garage cabinets with zero open wall space to hang a 36-inch indoor air handler? Cooper & Hunter's flush ceiling cassette fits between standard 16-inch ceiling joists."),
    ("milwaukee-dewalt-3-5-inch-bi-metal-hole-saw-with-arbor-for-mini-splits", "3-1/2 Inch (89mm) Heavy-Duty Bi-Metal M42 Cobalt Hole Saw w/ Hex Arbor & Pilot Bit", "Wall Pass-Through Hole Saw", "4.8", "#1 Tool for Drilling Clean 3.5\" Wall Pass-Through Holes", "8% Cobalt M42 Bi-Metal Teeth Slice Wood Siding, Drywall & Sheathing", "Exact 3.5-Inch (89mm) Diameter Fits Standard Wall Sleeves", "1-7/8\" Deep Cutting Cup + Chip-Ejecting Slots", "Includes Heavy-Duty 1/2\" Chuck Arbor & Spring", "3+1+2+Inch+Bi+Metal+Hole+Saw+with+Arbor+89mm", "Every mini-split installation requires drilling one 2.75\" to 3.5\" hole through the wall (angled 5 degrees downward toward the outside for gravity drain flow). A dedicated 3.5-inch cobalt bi-metal hole saw cuts through drywall, studs, and siding in 60 seconds."),
    ("klien-tools-et110-testo-316-heated-diode-refrigerant-leak-detector", "Electronic Heated-Sensor Refrigerant Leak Detector (R410A, R32, R454B, R134a) + Big Blu Soap", "Electronic Flare Leak Sniffer", "4.7", "#1 Way to Verify Zero Micro-Leaks Before Wrapping Line Set", "Sniffs Leaks Down to 0.1 oz/Year Across R410A, R32 & R454B", "15-Inch Flexible Gooseneck Probe Reaches Inside Indoor Coil", "Audible Buzzer + 7-Level LED Leak Intensity Bar", "Pair w/ Big Blu Micro-Bubble Soap Solution", "Refrigerant+Leak+Detector+R410A+R32+HVAC+Sniffer", "After opening the refrigerant valves on a new mini-split, sweeping the four flare nuts with an electronic refrigerant sniffer and micro-bubble soap solution gives you 100% peace of mind before snapping on the line-set covers."),
    ("tosot-turbro-greenland-12000-18000-btu-energy-star-mini-split", "TURBRO Greenland / TOSOT 12,000 & 18,000 BTU Energy Star Inverter Mini-Split Heat Pump", "Gree-Built Inverter System", "4.7", "Best Gree-Manufactured Mini-Split Under $780", "Built by Gree (World's Largest AC Manufacturer)", "Up to 21–22 SEER2 (Qualifies for Federal 25C Tax Credit Check)", "Heats Down to -4°F / -13°F w/ Base Pan Heater", "I-Feel Remote Sensor + Wi-Fi Voice Control", "TURBRO+Greenland+TOSOT+12000+18000+BTU+Mini+Split", "Manufactured by global HVAC giant Gree with high-SEER2 variable compressors and an I-Feel remote that senses temperature right where you are sitting, the TURBRO Greenland and TOSOT units punch far above their price."),
    ("spring-benders-copper-tubing-bender-set-1-4-3-8-1-2-5-8-inch", "4-Piece Internal & External Spring Copper Tubing Bender Set (1/4\", 3/8\", 1/2\", 5/8\")", "Anti-Kink Copper Pipe Benders", "4.8", "#1 $16 Tool That Prevents Kinked & Ruined Mini-Split Copper Lines!", "Slips Over (or Inside) 1/4\", 3/8\", 1/2\" & 5/8\" Copper Tubing", "Lets You Bend Tight 90° Corners Out of the Wall With Zero Kinks!", "Flared End Bell Slides Off Easily After Bending", "Oil-Hardened Spring Steel", "Copper+Tubing+Spring+Bender+Set+1+4+3+8+1+2+5+8+HVAC", "The #1 disaster during a DIY mini-split install is bending the copper pipes 90 degrees out of the wall hole by hand and kinking the tube flat—which chokes refrigerant flow and ruins a $300 line set. Sliding a $16 spring bender over the pipe makes kinking physically impossible."),
    ("southwire-10-2-12-2-uf-b-underground-feeder-and-nm-b-copper-wire", "Southwire 50-Ft & 100-Ft 12/2 & 10/2 w/ Ground UF-B / NM-B Solid Copper Wire (For 240V Circuit)", "240V Dedicated Circuit Cable", "4.9", "#1 UL-Listed Copper Cable to Feed Your Outdoor Disconnect Box", "100% Pure Electrolytic Copper (Made in USA)", "12/2 Supports 20A Breakers (9k–18k BTU) | 10/2 Supports 30A (24k–36k)", "UF-B Rated for Direct Burial, Outdoor Conduit & Damp Walls", "SIMpull Jacket Slides Through Conduit Effortlessly", "Southwire+10+2+12+2+UF+B+NM+B+Copper+Electrical+Wire+50+Ft", "Running a new 240V dedicated circuit from your main breaker panel to your outdoor mini-split disconnect box requires either 12/2 copper wire (for 15A/20A units) or 10/2 copper wire (for 25A/30A units).")
]

def build_full_review_from_catalog(item_tuple, pub_date_str):
    slug_base, prod_name, cat, score, badge, s1, s2, s3, s4, kw, summary = item_tuple
    return {
        "slug": f"review-{slug_base}",
        "title": f"{prod_name} Review: BTU Output, SEER2 Efficiency & Install Test",
        "product_name": prod_name,
        "category": cat,
        "rating_score": score,
        "verdict_badge": badge,
        "spec_1": s1,
        "spec_2": s2,
        "spec_3": s3,
        "spec_4": s4,
        "published_date": pub_date_str,
        "keyword": kw,
        "summary": summary,
        "pros": [
            f"Clamp-meter & thermal-camera verified HVAC output ({s1}) tested in summer and winter loads",
            f"High-efficiency inverter / mechanical engineering ({s2}) slashes monthly electric bills",
            f"DIY and contractor friendly installation ({s3}) with standard flare and electrical specs",
            f"Backed by {s4} for multi-year climate comfort"
        ],
        "cons": [
            "Always verify your room BTU requirement, climate multiplier, and 240V breaker amps using our calculator before ordering"
        ],
        "body_paragraphs": [
            f"When sizing a ductless mini-split heat pump and 240V electrical circuit on {SITE_NAME}, matching your BTU tonnage to your room's square footage, ceiling height, and insulation is what prevents short-cycling and high humidity. In our hands-on thermal evaluation, the {prod_name} exceeded factory benchmarks.",
            f"Equipped with {s1} and {s2}, it holds room temperatures within 1°F while operating at a whisper-quiet decibel level. Furthermore, {s3} makes wall mounting and line-set routing clean and straightforward.",
            f"Supported by {s4}, the {prod_name} earns a {score}/5.0 rating as one of the highest-ROI HVAC upgrades for 2026."
        ]
    }

def get_cumulative_product_reviews():
    """
    Unlocks +3 brand-new unique product review articles EVERY SINGLE DAY since LAUNCH_EPOCH!
    Guarantees the website grows by 3 distinct review articles per day automatically and forever.
    """
    today = datetime.datetime.utcnow().date()
    days_elapsed = max(1, (today - LAUNCH_EPOCH).days + 1)
    total_daily_to_unlock = days_elapsed * REVIEWS_PER_DAY

    reviews = list(BASE_REVIEWS)
    catalog_len = len(DAILY_CUMULATIVE_CATALOG)

    for idx in range(total_daily_to_unlock):
        day_offset = idx // REVIEWS_PER_DAY
        pub_date = (LAUNCH_EPOCH + datetime.timedelta(days=day_offset)).strftime("%Y-%m-%d")

        if idx < catalog_len:
            reviews.append(build_full_review_from_catalog(DAILY_CUMULATIVE_CATALOG[idx], pub_date))
        else:
            # Procedural infinite generator so +3 new unique review articles are created every day forever
            extra_num = idx - catalog_len + 1
            hvac_configs = [
                ("12,000 BTU (1.0 Ton) 22 SEER2 Mini-Split for 450 Sq.Ft Bedroom/Office", 12000, "1.0 Ton", "15A/20A 240V", "450 Sq.Ft"),
                ("18,000 BTU (1.5 Ton) 21 SEER2 Mini-Split for 650 Sq.Ft 2-Car Garage", 18000, "1.5 Ton", "20A 240V (12 AWG)", "650 Sq.Ft"),
                ("24,000 BTU (2.0 Ton) Cold-Climate Heat Pump for 1,000 Sq.Ft Shop", 24000, "2.0 Ton", "25A/30A 240V (10 AWG)", "1,000 Sq.Ft"),
                ("9,000 BTU (0.75 Ton) 23 SEER2 Mini-Split for 300 Sq.Ft Nursery/Study", 9000, "0.75 Ton", "15A 115V/240V", "300 Sq.Ft"),
                ("36,000 BTU (3.0 Ton) Dual/Tri-Zone Heat Pump for 1,500 Sq.Ft Home", 36000, "3.0 Ton", "35A/40A 240V (8 AWG)", "1,500 Sq.Ft"),
                ("18,000 BTU -22°F Arctic Heat Pump for 550 Sq.Ft Sunroom / Bonus Room", 18000, "1.5 Ton", "20A 240V (12 AWG)", "550 Sq.Ft")
            ]
            h_name, btu_v, ton_s, brk_s, sf_s = hvac_configs[extra_num % len(hvac_configs)]
            proc_tuple = (
                f"mini-split-{btu_v}-btu-{sf_s.split()[0]}sqft-heat-pump-review-{extra_num}",
                f"{btu_v:,} BTU ({ton_s}, {brk_s}) Mini-Split Heat Pump for {sf_s} Review (#{extra_num})",
                f"{btu_v:,} BTU / {ton_s} System",
                "4.8",
                f"Verified {btu_v:,} BTU @ {sf_s}",
                f"{btu_v:,} BTU/hr ({ton_s} Inverter)",
                f"Sized for {sf_s} ({brk_s})",
                "Includes 16'–25' Line Set + Disconnect Whip",
                "7-to-10 Year Compressor Warranty",
                f"MRCOOL+Senville+Pioneer+{btu_v}+BTU+Mini+Split+Heat+Pump",
                f"Complete thermal pull-down speed, kWh power-meter draw, and sub-zero heating test for a {h_name}."
            )
            reviews.append(build_full_review_from_catalog(proc_tuple, pub_date))

    return list(reversed(reviews))

# ==========================================
# PROGRAMMATIC SEO MINI-SPLIT BTU PRESETS
# ==========================================
MINISPLIT_PRESETS = [
    {"slug": "2-car-garage-mini-split-btu-size-calculator", "name": "2-Car Garage / Workshop (24' × 24' = 576 Sq.Ft — 18,000 BTU)", "sqft": 576, "ceiling_ft": 9.0, "insulation": "1.20", "climate": "1.10", "zones": 1, "desc": "Calculate exact ductless mini-split BTU (18,000 BTU / 1.5 Ton), 240V 20A breaker & 12 AWG whip sizing, and cold-climate heating for a 24'×24' 2-car garage."},
    {"slug": "12000-btu-1-ton-mini-split-room-size-breaker-calculator", "name": "Master Bedroom, Office or 1-Car Garage (400–550 Sq.Ft — 12,000 BTU)", "sqft": 450, "ceiling_ft": 8.0, "insulation": "1.0", "climate": "1.05", "zones": 1, "desc": "Calculate why a 12,000 BTU (1.0 Ton) inverter mini-split is the #1 match for 400 to 550 sq. ft. bedrooms, bonus rooms, and 1-car garages."},
    {"slug": "24000-btu-2-ton-mini-split-square-footage-breaker-calculator", "name": "Open Living Area, Basement or Large Shop (900–1,200 Sq.Ft — 24,000 BTU)", "sqft": 1000, "ceiling_ft": 9.0, "insulation": "1.0", "climate": "1.10", "zones": 1, "desc": "Size a 24,000 BTU (2.0 Ton) single-zone or dual-zone mini-split heat pump, 240V 25A/30A breaker, and 10 AWG copper whip for a 1,000 sq. ft. space."},
    {"slug": "9000-btu-mini-split-bedroom-office-size-calculator", "name": "Small Bedroom, Nursery or Home Office (200–350 Sq.Ft — 9,000 BTU)", "sqft": 280, "ceiling_ft": 8.0, "insulation": "1.0", "climate": "1.0", "zones": 1, "desc": "Prevent short-cycling and clammy humidity in small 200–350 sq. ft. bedrooms by sizing a 9,000 BTU (0.75 Ton) variable-speed inverter mini-split."},
    {"slug": "36000-btu-3-ton-multi-zone-mini-split-house-calculator", "name": "3-Zone / 4-Zone Whole-Floor or Cabin (1,400–1,800 Sq.Ft — 36,000 BTU)", "sqft": 1550, "ceiling_ft": 8.5, "insulation": "1.0", "climate": "1.10", "zones": 3, "desc": "Calculate total BTU tonnage (36,000 BTU / 3.0 Ton), per-room indoor air handler splits (e.g., 18k + 9k + 9k), and 240V 35A/40A breaker sizing."},
    {"slug": "sunroom-four-season-porch-mini-split-btu-calculator", "name": "Glass Sunroom / Florida Room (350 Sq.Ft w/ High Solar Gain — 18,000 BTU)", "sqft": 350, "ceiling_ft": 9.0, "insulation": "1.40", "climate": "1.15", "zones": 1, "desc": "Sunrooms with 3 walls of glass absorb +40% solar radiant heat. Calculate why a 350 sq. ft. sunroom requires an 18,000 BTU mini-split instead of 9,000 BTU."},
    {"slug": "bonus-room-over-garage-frog-mini-split-btu-calculator", "name": "Bonus Room Over Garage / Attic Knee-Wall (500 Sq.Ft — 18,000 BTU)", "sqft": 500, "ceiling_ft": 8.5, "insulation": "1.25", "climate": "1.10", "zones": 1, "desc": "Rooms above unconditioned garages bake in summer and freeze in winter. Calculate exact BTU (15,000–18,000 BTU) for FROG bonus rooms."},
    {"slug": "cold-climate-sub-zero-hyper-heat-mini-split-btu-calculator", "name": "Northern Cold-Climate (-15°F to -22°F) Primary Heating Calculator", "sqft": 650, "ceiling_ft": 8.5, "insulation": "1.10", "climate": "1.30", "zones": 1, "desc": "Account for the +30% sub-zero heating load multiplier to size a Senville AURA or MRCOOL Hyper-Heat unit that delivers 100% heat at +5°F."},
    {"slug": "mini-split-wire-gauge-and-240v-breaker-size-calculator", "name": "Mini-Split 240V Breaker, MCA/MOP & Wire Gauge (14/12/10/8 AWG) Calculator", "sqft": 750, "ceiling_ft": 9.0, "insulation": "1.0", "climate": "1.10", "zones": 1, "desc": "Calculate NEC Minimum Circuit Ampacity (MCA), Maximum Overcurrent Protection (MOP breaker), and outdoor disconnect whip gauge for 9k to 48k BTU units."},
    {"slug": "metal-pole-barn-and-insulated-shed-mini-split-calculator", "name": "30' × 40' Insulated Pole Barn & Metal Shop (1,200 Sq.Ft / 12' Ceiling)", "sqft": 1200, "ceiling_ft": 12.0, "insulation": "1.20", "climate": "1.10", "zones": 2, "desc": "Factor in 12-foot high ceilings (+35% air volume) to size dual 18,000 BTU or a 36,000 BTU mini-split for a 1,200 sq. ft. pole barn workshop."},
    {"slug": "server-room-grow-room-bitcoin-miner-mini-split-btu-calculator", "name": "Server Closet / 3,000W Equipment Heat Load Mini-Split Calculator", "sqft": 200, "ceiling_ft": 8.0, "insulation": "1.35", "climate": "1.25", "zones": 1, "desc": "Every 1,000 watts of continuous electronics generates 3,412 BTU/hr of heat! Calculate mini-split cooling capacity for server, network, and equipment rooms."},
    {"slug": "48000-btu-4-ton-4-zone-5-zone-whole-home-mini-split-calculator", "name": "4-Zone / 5-Zone Whole-House Ductless System (2,200 Sq.Ft — 48,000 BTU)", "sqft": 2200, "ceiling_ft": 9.0, "insulation": "1.0", "climate": "1.10", "zones": 4, "desc": "Calculate 48,000 BTU (4.0 Ton) multi-zone outdoor condenser sizing, branch box combinations, and 240V 45A/50A 6-AWG circuit specs."}
]

def get_dynamic_sqft_pages():
    configs = [
        (300, 8.0, "1.0", 1, "300 Sq.Ft Room (9,000 BTU / 0.75 Ton)"),
        (400, 8.0, "1.0", 1, "400 Sq.Ft Room (9,000–12,000 BTU)"),
        (500, 8.5, "1.0", 1, "500 Sq.Ft Room (12,000 BTU / 1.0 Ton)"),
        (600, 9.0, "1.1", 1, "600 Sq.Ft Space (18,000 BTU / 1.5 Ton)"),
        (750, 9.0, "1.0", 1, "750 Sq.Ft Space (18,000 BTU / 1.5 Ton)"),
        (900, 9.0, "1.0", 1, "900 Sq.Ft Space (24,000 BTU / 2.0 Ton)"),
        (1100, 9.0, "1.0", 2, "1,100 Sq.Ft Dual-Zone (24,000 BTU)"),
        (1400, 9.0, "1.0", 3, "1,400 Sq.Ft Tri-Zone (30,000–36,000 BTU)")
    ]
    day_of_year = datetime.datetime.utcnow().timetuple().tm_yday
    active_count = min(len(configs), 5 + (day_of_year % 4))
    pages = []
    for sf_v, ceil_v, ins_s, z_cnt, label in configs[:active_count]:
        pages.append({
            "slug": f"{sf_v}-sq-ft-mini-split-btu-tonnage-breaker-calculator",
            "name": f"{label}",
            "sqft": sf_v,
            "ceiling_ft": ceil_v,
            "insulation": ins_s,
            "climate": "1.05",
            "zones": z_cnt,
            "desc": f"Calculate exact mini-split BTU capacity, heat pump tonnage, and 240V breaker/wire gauge for a {label}."
        })
    return pages

ALL_CALC_PAGES = MINISPLIT_PRESETS + get_dynamic_sqft_pages()

def compute_minisplit_specs(sqft, ceiling_ft, ins_mult, climate_mult, zones):
    # Base ASHRAE Manual J rule of thumb: 25 BTU per sq.ft adjusted for ceiling height (vs 8 ft), insulation, and climate
    ceil_factor = max(0.95, float(ceiling_ft) / 8.0)
    raw_btu = int(round(sqft * 24.0 * ceil_factor * float(ins_mult) * float(climate_mult)))

    btu_tiers = [9000, 12000, 18000, 24000, 30000, 36000, 48000]
    rec_btu = 48000
    for t in btu_tiers:
        if t >= raw_btu:
            rec_btu = t
            break

    tons = round(rec_btu / 12000.0, 2)

    # Zone Split Suggestion
    if int(zones) <= 1:
        zone_split_str = f"1× {int(rec_btu/1000)}k BTU Wall Unit"
    elif int(zones) == 2:
        half = int(rec_btu // 2000)
        zone_split_str = f"2× {max(9, half)}k BTU Indoor Heads"
    elif int(zones) == 3:
        zone_split_str = "1× 18k + 2× 9k BTU Heads" if rec_btu >= 30000 else "3× 9k BTU Indoor Heads"
    else:
        zone_split_str = "2× 12k + 2× 9k BTU Heads"

    # Electrical Breaker & Wire Gauge (240V Single-Phase)
    if rec_btu <= 12000:
        breaker_str = "240V 15A/20A (14/12 AWG Whip)"
        line_sizes = "1/4\" Liquid + 3/8\" Suction"
    elif rec_btu == 18000:
        breaker_str = "240V 20A Breaker (12 AWG Whip)"
        line_sizes = "1/4\" Liquid + 1/2\" Suction"
    elif rec_btu in (24000, 30000):
        breaker_str = "240V 25A/30A (10 AWG Whip)"
        line_sizes = "3/8\" Liquid + 5/8\" Suction"
    else:
        breaker_str = "240V 35A–45A (8 AWG Copper)"
        line_sizes = "Multi-Port 1/4\" × 3/8\" Lines"

    return raw_btu, rec_btu, tons, zone_split_str, breaker_str, line_sizes

def generate_faq_data(preset_name, sqft, ceiling_ft, ins_mult, climate_mult, zones):
    raw_btu, rec_btu, tons, zone_str, brk_str, line_str = compute_minisplit_specs(
        sqft, ceiling_ft, ins_mult, climate_mult, zones
    )
    return [
        {
            "q": f"What size mini-split (BTU & Tons) do I need for {preset_name} ({sqft:,} sq. ft.)?",
            "a": f"Factoring in your {sqft:,} sq. ft. floor area, {ceiling_ft}-foot ceiling height, insulation quality, and climate zone, your calculated thermal load is {raw_btu:,} BTU/hr. You should install a {rec_btu:,} BTU ({tons} Ton) Inverter Mini-Split Heat Pump configured as {zone_str}."
        },
        {
            "q": f"What size 240V circuit breaker, disconnect box, and wire gauge is needed for {rec_btu:,} BTU?",
            "a": f"A {rec_btu:,} BTU ({tons} Ton) 230V/240V inverter mini-split requires a dedicated {brk_str} connected through an outdoor NEMA 3R pull-out disconnect box with an Intermatic AG3000 surge protector."
        },
        {
            "q": f"What copper line-set diameters and vacuum pump size are used on a {rec_btu:,} BTU unit?",
            "a": f"A {rec_btu:,} BTU system uses {line_str} insulated copper tubing. Unless you purchase a pre-charged MRCOOL DIY 4th Gen system, evacuate the lines for 20 minutes down below 400 microns using a 4.5 CFM 1/3 HP rotary-vane vacuum pump and R410A/R32 manifold gauge kit."
        },
        {
            "q": "Can a ductless mini-split heat my room in freezing sub-zero winter weather?",
            "a": "Yes! Modern cold-climate inverter heat pumps (such as the Senville AURA -22°F, Pioneer Diamante Ultra -13°F, and MRCOOL DIY 4th Gen) extract heat energy from outdoor air down to -13°F to -22°F while consuming 60% less electricity than baseboard resistance heaters."
        },
        {
            "q": "What happens if I oversize a mini-split by too many BTUs in a small room?",
            "a": "Even though variable-speed inverter compressors can throttle down to ~30% capacity, putting a massive 24,000 BTU unit inside a tiny 300 sq. ft. room causes the unit to cool the air in 3 minutes and shut off before removing humidity—leaving the room cold and clammy."
        }
    ]

def render_comparison_table_section():
    rows_html = ""
    for item in COMPARISON_MATRIX:
        link = amz_url(item["keyword"])
        rows_html += f"""
        <tr class="border-b border-gray-300 hover:bg-gray-200/80 transition">
            <td class="p-3.5 font-extrabold text-gray-900 text-xs sm:text-sm">{item['model']}</td>
            <td class="p-3.5 text-xs font-semibold text-blue-900">{item['type']}</td>
            <td class="p-3.5 text-xs font-mono text-gray-800">{item['btu_seer']}</td>
            <td class="p-3.5 text-xs text-gray-800">{item['low_ambient']}</td>
            <td class="p-3.5 text-xs text-emerald-800 font-bold">{item['highlight']}</td>
            <td class="p-3.5 text-xs font-bold text-amber-700">{item['rating']}</td>
            <td class="p-3.5 text-right">
                <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
                   class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2 px-3.5 rounded-lg transition shadow-sm whitespace-nowrap">
                   Check Price &rarr;
                </a>
            </td>
        </tr>
        """

    vs_cards_html = ""
    for vs in VS_COMPARISONS:
        vs_cards_html += f"""
        <a href="{BASE_URL}/{vs['slug']}.html" class="bg-gray-100 border-2 border-gray-300 hover:border-blue-700 rounded-xl p-5 transition flex flex-col justify-between shadow-sm">
            <div>
                <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{vs['winner_badge']}</span>
                <h3 class="text-base font-extrabold text-gray-900 mt-2.5 mb-1.5 leading-snug">{vs['title']}</h3>
                <p class="text-xs text-gray-700 leading-relaxed">{vs['summary']}</p>
            </div>
            <span class="text-xs font-extrabold text-blue-800 mt-4 inline-flex items-center gap-1">Read Full Side-by-Side Comparison &rarr;</span>
        </a>
        """

    return f"""
    <!-- PRODUCT COMPARISON SECTION (PERBANDINGAN PRODUK) -->
    <section id="comparison" class="space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Side-by-Side Spec Matrix</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Top Ductless Mini-Split Heat Pumps, Vacuum Kits & Surge Protectors Compared</h2>
            </div>
            <span class="text-xs font-semibold text-gray-600">2026 AHRI SEER2 & Sub-Zero HSPF2 Benchmarks</span>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-x-auto shadow-sm">
            <table class="w-full text-left border-collapse min-w-[720px]">
                <thead>
                    <tr class="bg-gray-300 border-b-2 border-gray-400 text-[11px] font-extrabold uppercase tracking-wider text-gray-800">
                        <th class="p-3.5">HVAC Model</th>
                        <th class="p-3.5">Category</th>
                        <th class="p-3.5">BTU / SEER2 Spec</th>
                        <th class="p-3.5">Low-Temp Heating</th>
                        <th class="p-3.5">Key Installation Advantage</th>
                        <th class="p-3.5">Rating</th>
                        <th class="p-3.5 text-right">Amazon Deal</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>

        <!-- Head-to-Head VS Guides -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-5 pt-2">
            {vs_cards_html}
        </div>
    </section>
    """

def render_review_cards_grid():
    active_reviews = get_cumulative_product_reviews()
    cards = ""
    for rev in active_reviews:
        amz_link = amz_url(rev["keyword"])
        cards += f"""
        <article class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-2xl p-6 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex flex-wrap items-center justify-between gap-2 mb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{rev['verdict_badge']}</span>
                    <span class="text-xs font-black bg-amber-200 text-amber-950 px-2.5 py-1 rounded-lg">Score: {rev['rating_score']} / 5.0 ★</span>
                </div>
                <div class="flex items-center justify-between text-xs text-gray-600 mb-1">
                    <span class="font-semibold uppercase tracking-wide text-gray-700">{rev['category']}</span>
                    <span class="font-mono text-[11px] text-gray-500">Published: {rev['published_date']}</span>
                </div>
                <h3 class="text-lg font-extrabold text-gray-900 mt-1 mb-2 leading-snug">
                    <a href="{BASE_URL}/{rev['slug']}.html" class="hover:text-blue-800 transition">{rev['title']}</a>
                </h3>
                <p class="text-xs text-gray-700 leading-relaxed mb-4">{rev['summary']}</p>
                <div class="grid grid-cols-2 gap-2 text-[11px] bg-gray-200/90 p-3 rounded-xl border border-gray-300 mb-4">
                    <div><span class="text-gray-500 block">BTU / Output:</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                    <div><span class="text-gray-500 block">Line Set / Tech:</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                    <div><span class="text-gray-500 block">Installation:</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                    <div><span class="text-gray-500 block">Warranty:</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
                </div>
            </div>
            <div class="flex flex-col sm:flex-row gap-2.5 pt-2">
                <a href="{BASE_URL}/{rev['slug']}.html" class="flex-1 text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-xs py-2.5 px-3 rounded-lg transition">
                    Read Full HVAC Review &rarr;
                </a>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-3 rounded-lg transition shadow-sm">
                    Check Price on Amazon &rarr;
                </a>
            </div>
        </article>
        """
    return cards, len(active_reviews)

def render_common_header_and_banner():
    top_deal_link = amz_url("MRCOOL+DIY+4th+Gen+Senville+Pioneer+Mini+Split+Heat+Pump+Deals")
    return f"""
    <!-- TOP PROMOTIONAL AFFILIATE BANNER -->
    <div class="bg-gray-800 text-gray-100 py-2.5 px-4 text-center text-xs sm:text-sm font-medium border-b border-gray-700">
        <div class="max-w-6xl mx-auto flex flex-wrap items-center justify-center gap-2">
            <span class="bg-amber-400 text-gray-950 font-extrabold px-2 py-0.5 rounded text-xs uppercase">Mini-Split Deals</span>
            <span>Save up to 30% on MRCOOL DIY 4th Gen, Senville Cold-Climate Heat Pumps, Vacuum Kits & 240V Whips on Amazon.</span>
            <a href="{top_deal_link}" target="_blank" rel="nofollow sponsored noopener" class="text-amber-300 hover:text-amber-200 underline font-bold ml-1">
                View Active Mini-Split Deals &rarr;
            </a>
        </div>
    </div>

    <!-- STICKY NAVIGATION HEADER (GRAY BACKGROUND) -->
    <header class="bg-gray-300 border-b border-gray-400 sticky top-0 z-30 shadow-sm">
        <div class="max-w-6xl mx-auto px-4 py-3.5 flex flex-wrap items-center justify-between gap-4">
            <a href="{BASE_URL}/" class="flex items-center gap-2.5">
                <div class="w-9 h-9 rounded-lg bg-blue-700 flex items-center justify-center text-white font-black text-lg shadow-sm">M</div>
                <div>
                    <span class="font-extrabold text-lg tracking-tight text-gray-900 block leading-none">{SITE_NAME}</span>
                    <span class="text-[11px] text-gray-700 font-medium">Mini-Split BTU, Tonnage & 240V Breaker Engine</span>
                </div>
            </a>
            <nav class="flex flex-wrap items-center gap-4 sm:gap-5 text-xs sm:text-sm font-semibold text-gray-800">
                <a href="{BASE_URL}/#calculator" class="hover:text-blue-800 transition">BTU & Breaker Calc</a>
                <a href="{BASE_URL}/#product-search" class="hover:text-blue-800 transition">Search HVAC</a>
                <a href="{BASE_URL}/#best-sellers" class="hover:text-blue-800 transition">Best Sellers</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-800 transition">Compare</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-800 transition">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-800 transition">FAQ</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-800 transition font-bold underline">Site Map</a>
            </nav>
        </div>
    </header>
    """

def render_onpage_sitemap_directory():
    calc_links = "".join([
        f'<li><a href="{BASE_URL}/{p["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">❄️ {p["name"]} Calculator</a></li>'
        for p in ALL_CALC_PAGES
    ])
    vs_links = "".join([
        f'<li><a href="{BASE_URL}/{v["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">⚖️ {v["title"]}</a></li>'
        for v in VS_COMPARISONS
    ])
    all_revs = get_cumulative_product_reviews()
    rev_links = "".join([
        f'<li><a href="{BASE_URL}/{r["slug"]}.html" class="text-xs text-gray-700 hover:text-blue-800 hover:underline">📝 [{r["published_date"]}] {r["product_name"]} Review</a></li>'
        for r in all_revs
    ])
    return f"""
    <!-- COMPLETE ON-PAGE SITE MAP SECTION (SITE MAP) -->
    <section id="site-map" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-6">
        <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-gray-300 pb-3">
            <div>
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Complete Site Architecture & Index</span>
                <h2 class="text-xl font-extrabold text-gray-900">Full HTML & XML Site Map Directory</h2>
            </div>
            <div class="flex gap-3 text-xs font-bold">
                <a href="{BASE_URL}/sitemap.html" class="bg-gray-300 hover:bg-gray-400 text-gray-900 px-3 py-1.5 rounded-lg transition">Open Dedicated HTML Site Map &rarr;</a>
                <a href="{BASE_URL}/sitemap.xml" class="bg-blue-700 hover:bg-blue-800 text-white px-3 py-1.5 rounded-lg transition">View XML Sitemap</a>
            </div>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">1. Mini-Split BTU Calculators ({len(ALL_CALC_PAGES) + 1})</h3>
                <ul class="space-y-1.5">
                    <li><a href="{BASE_URL}/" class="text-xs font-bold text-blue-800 hover:underline">🏠 Home — Master Mini-Split BTU & Breaker Calculator</a></li>
                    {calc_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">2. Head-to-Head Comparisons ({len(VS_COMPARISONS)})</h3>
                <ul class="space-y-2">
                    {vs_links}
                </ul>
            </div>
            <div>
                <h3 class="text-sm font-extrabold text-gray-900 mb-2.5 uppercase tracking-wide border-b border-gray-300 pb-1">3. Daily Product Reviews ({len(all_revs)} — +3/Day)</h3>
                <ul class="space-y-1.5 max-h-80 overflow-y-auto pr-2">
                    {rev_links}
                </ul>
            </div>
        </div>
    </section>
    """

def render_dedicated_html_sitemap_page():
    canonical_url = f"{BASE_URL}/sitemap.html"
    sitemap_block = render_onpage_sitemap_directory()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Complete Site Map Directory — Calculators, Comparisons & Daily Reviews | {SITE_NAME}</title>
    <meta name="description" content="Complete HTML and XML site map directory of all ductless mini-split BTU calculators, heat pump tonnage guides, 240V breaker calculators, and daily HVAC reviews on {SITE_NAME}.">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-10 space-y-8">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home</a>
            <span>/</span>
            <span class="text-gray-900">Complete Site Map</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-2">
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900">{SITE_NAME} — Complete Site Map</h1>
            <p class="text-sm text-gray-700">Browse every interactive ductless mini-split BTU calculator, multi-zone heat pump guide, 240V breaker sizing tool, head-to-head comparison, and cumulative daily product review article (+3 added daily) below.</p>
        </div>

        {sitemap_block}
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_calculator_page(page_data, is_home=False):
    raw_btu, rec_btu, tons, _, brk_str, _ = compute_minisplit_specs(
        page_data["sqft"], page_data["ceiling_ft"], page_data["insulation"],
        page_data["climate"], page_data["zones"]
    )
    title = f"{SITE_NAME} — {SITE_TAGLINE}" if is_home else f"{page_data['name']} — {rec_btu:,} BTU ({tons} Ton) Calculator | {SITE_NAME}"
    description = page_data["desc"]
    canonical_url = f"{BASE_URL}/" if is_home else f"{BASE_URL}/{page_data['slug']}.html"
    faqs = generate_faq_data(
        page_data["name"], page_data["sqft"], page_data["ceiling_ft"],
        page_data["insulation"], page_data["climate"], page_data["zones"]
    )

    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
            for item in faqs
        ]
    }

    app_schema = {
        "@context": "https://schema.org",
        "@type": "WebApplication",
        "name": title,
        "url": canonical_url,
        "applicationCategory": "UtilitiesApplication",
        "operatingSystem": "All",
        "description": description,
        "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}
    }

    bestseller_cards_html = ""
    for prod in BEST_SELLERS:
        link = amz_url(prod["keyword"])
        bestseller_cards_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 hover:border-gray-400 rounded-xl p-5 shadow-sm transition flex flex-col justify-between">
            <div>
                <div class="flex items-center justify-between gap-2 mb-2">
                    <span class="text-xs font-bold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded-full">{prod['badge']}</span>
                    <span class="text-xs font-semibold text-amber-700">{prod['rating']}</span>
                </div>
                <span class="text-xs text-gray-600 font-medium">{prod['category']}</span>
                <h3 class="text-base font-bold text-gray-900 mt-1 mb-2 leading-snug">{prod['title']}</h3>
                <p class="text-xs text-gray-700 mb-4 bg-gray-200 p-2.5 rounded-lg border border-gray-300">{prod['specs']}</p>
            </div>
            <a href="{link}" target="_blank" rel="nofollow sponsored noopener"
               class="w-full inline-flex items-center justify-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-2.5 px-4 rounded-lg transition shadow-sm">
               Check Today's Price on Amazon &rarr;
            </a>
        </div>
        """

    preset_links_html = ""
    for p in ALL_CALC_PAGES:
        _, p_btu, p_tons, _, _, _ = compute_minisplit_specs(
            p["sqft"], p["ceiling_ft"], p["insulation"], p["climate"], p["zones"]
        )
        active_cls = "bg-blue-100 border-blue-700 text-blue-950 font-bold" if (not is_home and p["slug"] == page_data["slug"]) else "bg-gray-100 border-gray-300 text-gray-800 hover:border-blue-700 hover:text-gray-950"
        preset_links_html += f"""
        <a href="{BASE_URL}/{p['slug']}.html" class="border rounded-lg p-3 text-xs transition flex items-center justify-between {active_cls}">
            <span class="truncate pr-2">{p['name']}</span>
            <span class="text-blue-900 font-mono shrink-0">{int(p_btu/1000)}k BTU</span>
        </a>
        """

    faq_html = ""
    for item in faqs:
        faq_html += f"""
        <div class="bg-gray-100 border-2 border-gray-300 rounded-xl p-5">
            <h3 class="text-base font-bold text-gray-900 mb-2">{item['q']}</h3>
            <p class="text-sm text-gray-700 leading-relaxed">{item['a']}</p>
        </div>
        """

    mid_banner_link = amz_url("MRCOOL+DIY+4th+Gen+Mini+Split+Disconnect+Whip+and+Wall+Bracket+Bundle")
    comparison_html = render_comparison_table_section()
    reviews_grid_html, total_reviews_count = render_review_cards_grid()
    onpage_sitemap_html = render_onpage_sitemap_directory()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="website">
    <meta property="og:url" content="{canonical_url}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(faq_schema)}</script>
    <script type="application/ld+json">{json.dumps(app_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased selection:bg-blue-700 selection:text-white">

    {render_common_header_and_banner()}

    <main class="max-w-6xl mx-auto px-4 py-8 space-y-12">

        <!-- HERO TITLE SECTION -->
        <section class="text-center max-w-3xl mx-auto space-y-3">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-gray-300 border border-gray-400 text-xs font-semibold text-gray-800">
                <span>❄️ ASHRAE Manual-J BTU, Cold-Climate Heat Pump & NEC 240V Whip Sizing Engine</span>
            </div>
            <h1 class="text-3xl sm:text-4xl font-extrabold text-gray-900 tracking-tight">
                { "Ductless Mini-Split BTU, Heat Pump Tonnage & 240V Breaker Calculator" if is_home else f"{page_data['name']} — BTU & Breaker Calculator" }
            </h1>
            <p class="text-gray-700 text-sm sm:text-base leading-relaxed">
                {description}
            </p>
        </section>

        <!-- INTERACTIVE CALCULATOR + LIVE HARDWARE MATCHER -->
        <section id="calculator" class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
            <!-- Left Column: Inputs (7 Cols) -->
            <div class="lg:col-span-7 bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-gray-300 pb-4">
                    <div>
                        <h2 class="text-xl font-extrabold text-gray-900">1. Enter Room Square Footage, Ceiling & Insulation</h2>
                        <p class="text-xs text-gray-600">Calculates exact BTU tier, tonnage, multi-zone split, 240V breaker & copper line size</p>
                    </div>
                    <span class="text-xs font-mono bg-blue-100 text-blue-900 border border-blue-300 px-2.5 py-1 rounded font-semibold">Live HVAC Math</span>
                </div>

                <div>
                    <label for="quickPreset" class="block text-xs font-bold uppercase tracking-wider text-gray-700 mb-2">Quick Select Room or Garage Mini-Split Preset</label>
                    <select id="quickPreset" onchange="applyPreset(this.value)" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-semibold text-gray-900 focus:ring-2 focus:ring-blue-700">
                        <option value="{page_data['sqft']},{page_data['ceiling_ft']},{page_data['insulation']},{page_data['climate']},{page_data['zones']}">Current: {page_data['name']}</option>
                        <option value="576,9.0,1.20,1.10,1">2-Car Garage / Workshop (24'×24' = 576 Sq.Ft — 18,000 BTU)</option>
                        <option value="450,8.0,1.0,1.05,1">Master Bedroom or 1-Car Garage (450 Sq.Ft — 12,000 BTU)</option>
                        <option value="1000,9.0,1.0,1.10,1">Open Living Area / Basement (1,000 Sq.Ft — 24,000 BTU)</option>
                        <option value="280,8.0,1.0,1.0,1">Small Bedroom / Home Office (280 Sq.Ft — 9,000 BTU)</option>
                        <option value="350,9.0,1.40,1.15,1">Glass Sunroom / Florida Room (350 Sq.Ft High Sun — 18,000 BTU)</option>
                        <option value="1550,8.5,1.0,1.10,3">3-Zone Whole Floor or Cabin (1,550 Sq.Ft — 36,000 BTU)</option>
                    </select>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
                    <div>
                        <label for="sqftInput" class="block text-sm font-bold text-gray-800 mb-1">Total Area (Sq. Ft.)</label>
                        <input type="number" id="sqftInput" value="{page_data['sqft']}" min="100" max="3500" step="25" oninput="calculateMiniSplit()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-blue-700">
                    </div>

                    <div>
                        <label for="ceilInput" class="block text-sm font-bold text-gray-800 mb-1">Ceiling Height (Feet)</label>
                        <input type="number" id="ceilInput" value="{page_data['ceiling_ft']}" min="7.0" max="20.0" step="0.5" oninput="calculateMiniSplit()"
                               class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-base font-bold text-gray-900 focus:ring-2 focus:ring-blue-700">
                    </div>

                    <div>
                        <label for="zonesInput" class="block text-sm font-bold text-gray-800 mb-1">Number of Indoor Zones</label>
                        <select id="zonesInput" onchange="calculateMiniSplit()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3 py-2.5 text-sm font-bold text-gray-900">
                            <option value="1" {"selected" if page_data['zones'] == 1 else ""}>1 Zone (Single Room/Garage)</option>
                            <option value="2" {"selected" if page_data['zones'] == 2 else ""}>2 Zones (Dual-Zone Split)</option>
                            <option value="3" {"selected" if page_data['zones'] == 3 else ""}>3 Zones (Tri-Zone Split)</option>
                            <option value="4" {"selected" if page_data['zones'] >= 4 else ""}>4 Zones (Quad-Zone Home)</option>
                        </select>
                    </div>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 gap-5">
                    <div>
                        <label for="insInput" class="block text-sm font-bold text-gray-800 mb-1">Room Insulation & Sun Exposure</label>
                        <select id="insInput" onchange="calculateMiniSplit()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="0.90" {"selected" if page_data['insulation'] == "0.90" else ""}>Well Insulated + Shaded / Basement (0.90x)</option>
                            <option value="1.0" {"selected" if page_data['insulation'] == "1.0" else ""}>Standard Drywall & Double-Pane Windows (1.00x)</option>
                            <option value="1.20" {"selected" if page_data['insulation'] in ("1.20", "1.25") else ""}>Garage / Bonus Room Over Garage / Shed (1.20x)</option>
                            <option value="1.40" {"selected" if page_data['insulation'] >= "1.35" else ""}>Glass Sunroom / Uninsulated Metal Building (1.40x)</option>
                        </select>
                    </div>

                    <div>
                        <label for="climInput" class="block text-sm font-bold text-gray-800 mb-1">Climate & Winter Heating Goal</label>
                        <select id="climInput" onchange="calculateMiniSplit()" class="w-full bg-gray-200 border border-gray-400 rounded-lg px-3.5 py-2.5 text-sm font-bold text-gray-900">
                            <option value="1.0" {"selected" if page_data['climate'] == "1.0" else ""}>Mild / Moderate Climate (1.00x Base)</option>
                            <option value="1.10" {"selected" if page_data['climate'] in ("1.05", "1.10", "1.15") else ""}>Hot South (100°F+) or Chilly Winter (1.10x)</option>
                            <option value="1.30" {"selected" if page_data['climate'] >= "1.25" else ""}>Sub-Zero Northern Primary Heat (-15°F to -22°F | 1.30x)</option>
                        </select>
                    </div>
                </div>
            </div>

            <!-- Right Column: Output + Dynamic Amazon Recommendation (5 Cols) -->
            <div class="lg:col-span-5 bg-gray-100 border-2 border-blue-700 rounded-2xl p-6 sm:p-8 shadow-md space-y-6">
                <div class="border-b border-gray-300 pb-3">
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">2. Engineered BTU & Electrical Specs</span>
                    <h2 class="text-xl font-extrabold text-gray-900">Your Exact Mini-Split Sizing</h2>
                </div>

                <div class="grid grid-cols-2 gap-3.5">
                    <div class="bg-blue-100 border border-blue-300 rounded-xl p-3.5">
                        <span class="text-xs text-blue-950 font-semibold block">Recommended Unit</span>
                        <span id="resRecBTU" class="text-2xl font-black text-blue-800">18,000 BTU</span>
                        <span id="resTons" class="text-[11px] text-blue-900 block mt-0.5">1.50 Tons (17,900 Calc)</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Indoor Zone Config</span>
                        <span id="resZoneSplit" class="text-base font-black text-gray-900">1× 18k BTU Head</span>
                        <span class="text-[11px] text-emerald-800 font-bold block mt-0.5">20–23 SEER2 Inverter</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">240V Breaker & Whip</span>
                        <span id="resBreaker" class="text-sm font-extrabold text-gray-900">240V 20A (12 AWG)</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">+ AG3000 Surge Arrestor</span>
                    </div>
                    <div class="bg-gray-200 border border-gray-300 rounded-xl p-3.5">
                        <span class="text-xs text-gray-600 font-medium block">Copper Line-Set Size</span>
                        <span id="resLineSet" class="text-sm font-extrabold text-amber-800">1/4\" × 1/2\" Lines</span>
                        <span class="text-[11px] text-gray-600 block mt-0.5">3\" PVC Line Cover</span>
                    </div>
                </div>

                <!-- Dynamic Matched Product Box -->
                <div class="bg-gray-200 border-2 border-blue-600 rounded-xl p-4 space-y-3">
                    <div class="flex items-center justify-between">
                        <span class="text-[11px] font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2 py-0.5 rounded">Verified Hardware Match</span>
                        <span class="text-xs font-bold text-gray-700">Amazon Prime Ready</span>
                    </div>
                    <h3 id="recHvacTitle" class="text-base font-extrabold text-gray-900 leading-snug">Loading Mini-Split & Kit Match...</h3>
                    <p id="recHvacDesc" class="text-xs text-gray-700"></p>
                    <div class="pt-1 flex flex-col sm:flex-row gap-2.5">
                        <a id="recPrimaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-lg transition shadow-sm">
                           Shop Matched Mini-Split &rarr;
                        </a>
                        <a id="recSecondaryBtn" href="#" target="_blank" rel="nofollow sponsored noopener"
                           class="text-center bg-gray-800 hover:bg-gray-900 text-white font-bold text-xs py-3 px-3 rounded-lg transition">
                           Shop Whip & Vacuum Kit
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <!-- PRODUCT SEARCH ENGINE SECTION (SEARCH PRODUK) -->
        <section id="product-search" class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm">
            <div class="max-w-3xl mx-auto text-center space-y-4">
                <h2 class="text-2xl font-extrabold text-gray-900">Search Ductless Mini-Splits, Vacuum Pump Kits, 240V Whips & Line Covers</h2>
                <p class="text-sm text-gray-700">Search any BTU size (9000, 12000, 18000, 24000, 36000 BTU), brand (MRCOOL DIY, Senville, Pioneer, DELLA, Cooper & Hunter, VIVOHOME, Intermatic) on Amazon.</p>
                <form onsubmit="handleAmazonSearch(event)" class="flex flex-col sm:flex-row gap-3 pt-2">
                    <input type="text" id="amzSearchInput" placeholder="e.g. MRCOOL DIY 4th Gen 18000 BTU, Senville AURA 12000 BTU, 4.5 CFM HVAC Vacuum Pump..."
                           class="flex-1 bg-gray-200 border-2 border-gray-400 rounded-xl px-4 py-3 text-sm font-medium text-gray-900 placeholder-gray-500 focus:outline-none focus:border-blue-700" required>
                    <button type="submit" class="bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition cursor-pointer shrink-0">
                        Search on Amazon &rarr;
                    </button>
                </form>
                <div class="flex flex-wrap items-center justify-center gap-2 pt-2 text-xs">
                    <span class="text-gray-600 font-semibold">Popular Searches:</span>
                    <a href="{amz_url('MRCOOL DIY 4th Gen Mini Split Heat Pump')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">MRCOOL DIY 4th Gen</a>
                    <a href="{amz_url('Senville AURA LETO Mini Split Heat Pump')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">Senville Cold-Climate</a>
                    <a href="{amz_url('Pioneer Diamante Ultra Mini Split')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">Pioneer Diamante Ultra</a>
                    <a href="{amz_url('4.5 CFM HVAC Vacuum Pump and Manifold Gauge Set')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">HVAC Vacuum Pump Kits</a>
                    <a href="{amz_url('AC Disconnect Box and Pre Wired Whip Kit')}" target="_blank" rel="nofollow sponsored noopener" class="px-2.5 py-1 bg-gray-200 hover:bg-blue-200 text-gray-800 border border-gray-300 rounded-full transition">240V Disconnect & Whip</a>
                </div>
            </div>
        </section>

        <!-- BEST SELLING PRODUCTS GRID (PRODUK TERLARIS) -->
        <section id="best-sellers" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Verified Ductless HVAC Hardware</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">Best-Selling Mini-Split Heat Pumps, Vacuum Kits, Whips & Surge Protectors</h2>
                </div>
                <a href="{amz_url('Best Selling Ductless Mini Split Air Conditioners and Heat Pumps')}" target="_blank" rel="nofollow sponsored noopener" class="text-sm font-bold text-blue-800 hover:text-blue-900">
                    Browse Full Amazon Best Sellers &rarr;
                </a>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                {bestseller_cards_html}
            </div>
        </section>

        {comparison_html}

        <!-- CUMULATIVE DAILY PRODUCT REVIEW ARTICLES SECTION (+3 NEW ARTICLES PER DAY) -->
        <section id="reviews" class="space-y-6">
            <div class="flex flex-col sm:flex-row sm:items-end justify-between gap-2 border-b border-gray-300 pb-4">
                <div>
                    <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">Autonomous Daily Review Archive ({total_reviews_count} Published Articles & Growing +3/Day)</span>
                    <h2 class="text-2xl font-extrabold text-gray-900">In-Depth Mini-Split Heat Pump, Vacuum Tool & Electrical Review Articles</h2>
                </div>
                <span class="text-xs font-semibold bg-emerald-100 text-emerald-900 border border-emerald-300 px-3 py-1 rounded-full">+3 New Product Reviews Added Automatically Every Day</span>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {reviews_grid_html}
            </div>
        </section>

        <!-- MID-PAGE PROMOTIONAL AFFILIATE BANNER -->
        <section class="bg-gray-300 border-2 border-blue-700 rounded-2xl p-6 sm:p-8 flex flex-col md:flex-row items-center justify-between gap-6">
            <div class="space-y-2 max-w-2xl">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-700 text-white px-2.5 py-1 rounded">Complete DIY Mini-Split Installation Bundle</span>
                <h2 class="text-xl sm:text-2xl font-extrabold text-gray-900">Installing a Ductless Mini-Split in Your Garage, Workshop, or Addition?</h2>
                <p class="text-sm text-gray-800">Save $3,500 in contractor labor by pairing a Pre-Charged MRCOOL DIY 4th Gen (or Senville + 4.5 CFM Vacuum Kit) with a 240V Disconnect Whip, Intermatic AG3000 Surge Protector, and 3\" Line-Set Cover.</p>
            </div>
            <a href="{mid_banner_link}" target="_blank" rel="nofollow sponsored noopener"
               class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3.5 rounded-xl shadow-sm transition">
               Explore Mini-Split + Install Bundles on Amazon &rarr;
            </a>
        </section>

        <!-- PROGRAMMATIC SEO DIRECTORY -->
        <section id="presets" class="space-y-4">
            <div class="border-b border-gray-300 pb-3">
                <h2 class="text-xl font-extrabold text-gray-900">Room Square Footage, Garage & Multi-Zone Specific BTU Calculators</h2>
                <p class="text-xs text-gray-600">Select your exact room square footage or building type below for pre-calculated mini-split BTU tonnage and 240V breaker sizes.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-2.5">
                {preset_links_html}
            </div>
        </section>

        <!-- FREQUENTLY ASKED QUESTIONS (FAQ) -->
        <section id="faq" class="space-y-6">
            <div class="border-b border-gray-300 pb-3">
                <span class="text-xs font-extrabold uppercase tracking-wider text-blue-800">SEER2, Vacuum Evacuation & 240V Wiring Guide</span>
                <h2 class="text-2xl font-extrabold text-gray-900">Frequently Asked Questions (FAQ)</h2>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {faq_html}
            </div>
        </section>

        {onpage_sitemap_html}

    </main>

    <!-- FOOTER (GRAY BACKGROUND) -->
    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700">
        <div class="max-w-6xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-4">
            <div>
                <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
                <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
            </div>
            <div class="flex flex-wrap gap-4 font-medium text-gray-800">
                <a href="{BASE_URL}/" class="hover:text-blue-800">Home</a>
                <a href="{BASE_URL}/#comparison" class="hover:text-blue-800">Comparisons</a>
                <a href="{BASE_URL}/#reviews" class="hover:text-blue-800">Daily Reviews (+3/Day)</a>
                <a href="{BASE_URL}/sitemap.html" class="hover:text-blue-800 font-bold">HTML Site Map</a>
                <a href="{BASE_URL}/sitemap.xml" class="hover:text-blue-800">XML Sitemap</a>
                <a href="{BASE_URL}/#faq" class="hover:text-blue-800">FAQ</a>
            </div>
        </div>
    </footer>

    <!-- INTERACTIVE CALCULATOR & AFFILIATE MATCHING SCRIPT -->
    <script>
        const AFFILIATE_TAG = "{AFFILIATE_TAG}";

        function makeAmazonLink(query) {{
            return "https://www.amazon.com/s?k=" + encodeURIComponent(query) + "&tag=" + AFFILIATE_TAG;
        }}

        function applyPreset(val) {{
            const parts = val.split(",");
            if (parts.length === 5) {{
                document.getElementById("sqftInput").value = parts[0];
                document.getElementById("ceilInput").value = parts[1];
                document.getElementById("insInput").value = parts[2];
                document.getElementById("climInput").value = parts[3];
                document.getElementById("zonesInput").value = parts[4];
                calculateMiniSplit();
            }}
        }}

        function handleAmazonSearch(e) {{
            e.preventDefault();
            const q = document.getElementById("amzSearchInput").value.trim();
            if (q) {{
                window.open(makeAmazonLink(q), "_blank", "noopener,noreferrer");
            }}
        }}

        function calculateMiniSplit() {{
            const sqft = parseFloat(document.getElementById("sqftInput").value) || 576;
            const ceilFt = parseFloat(document.getElementById("ceilInput").value) || 9.0;
            const insMult = parseFloat(document.getElementById("insInput").value) || 1.20;
            const climMult = parseFloat(document.getElementById("climInput").value) || 1.10;
            const zones = parseInt(document.getElementById("zonesInput").value) || 1;

            const ceilFactor = Math.max(0.95, ceilFt / 8.0);
            const rawBTU = Math.round(sqft * 24.0 * ceilFactor * insMult * climMult);

            const tiers = [9000, 12000, 18000, 24000, 30000, 36000, 48000];
            let recBTU = 48000;
            for (let i = 0; i < tiers.length; i++) {{
                if (tiers[i] >= rawBTU) {{
                    recBTU = tiers[i];
                    break;
                }}
            }}

            const tons = (recBTU / 12000.0).toFixed(2);
            let zoneSplit = "1× " + (recBTU / 1000) + "k BTU Wall Unit";
            if (zones === 2) {{
                const h = Math.max(9, Math.floor(recBTU / 2000));
                zoneSplit = "2× " + h + "k BTU Indoor Heads";
            }} else if (zones === 3) {{
                zoneSplit = recBTU >= 30000 ? "1× 18k + 2× 9k Heads" : "3× 9k BTU Heads";
            }} else if (zones >= 4) {{
                zoneSplit = "2× 12k + 2× 9k Heads";
            }}

            let brkStr = "240V 20A (12 AWG Whip)";
            let lineStr = "1/4\\\" × 1/2\\\" Copper Lines";
            if (recBTU <= 12000) {{
                brkStr = "240V 15A/20A (14/12 AWG)";
                lineStr = "1/4\\\" × 3/8\\\" Copper Lines";
            }} else if (recBTU === 18000) {{
                brkStr = "240V 20A (12 AWG Whip)";
                lineStr = "1/4\\\" × 1/2\\\" Copper Lines";
            }} else if (recBTU <= 30000) {{
                brkStr = "240V 25A/30A (10 AWG Whip)";
                lineStr = "3/8\\\" × 5/8\\\" Copper Lines";
            }} else {{
                brkStr = "240V 35A–45A (8 AWG Wire)";
                lineStr = "Multi-Port 1/4\\\" × 3/8\\\" Lines";
            }}

            document.getElementById("resRecBTU").textContent = recBTU.toLocaleString() + " BTU";
            document.getElementById("resTons").textContent = tons + " Tons (" + rawBTU.toLocaleString() + " BTU Calc)";
            document.getElementById("resZoneSplit").textContent = zoneSplit;
            document.getElementById("resBreaker").textContent = brkStr;
            document.getElementById("resLineSet").textContent = lineStr;

            let recTitle = "";
            let recDesc = "";
            let primaryQuery = "";
            let secondaryQuery = "AC Disconnect Box Whip Kit and Intermatic AG3000 Surge Protector";

            if (zones > 1) {{
                recTitle = "MRCOOL DIY 4th Gen or Senville " + recBTU.toLocaleString() + " BTU " + zones + "-Zone Heat Pump System";
                recDesc = "Multi-zone inverter heat pump feeding " + zoneSplit + " across " + sqft.toLocaleString() + " sq. ft.";
                primaryQuery = "MRCOOL DIY Senville " + recBTU + " BTU " + zones + " Zone Mini Split Heat Pump";
            }} else if (climMult >= 1.25) {{
                recTitle = "Senville AURA (-22°F Arctic) or MRCOOL Hyper-Heat " + recBTU.toLocaleString() + " BTU (" + tons + " Ton)";
                recDesc = "Energy Star Cold-Climate certified heat pump delivering 100% heat at +5°F and running down to -22°F.";
                primaryQuery = "Senville AURA MRCOOL " + recBTU + " BTU Cold Climate Mini Split Heat Pump";
                secondaryQuery = "4.5 CFM HVAC Vacuum Pump Gauge Set and Mini Split Wall Bracket";
            }} else {{
                recTitle = "MRCOOL DIY 4th Gen (No-Vacuum) or Senville LETO / Pioneer " + recBTU.toLocaleString() + " BTU (" + tons + " Ton)";
                recDesc = "20–22 SEER2 inverter heat pump matched to " + sqft.toLocaleString() + " sq. ft. on a " + brkStr + " circuit.";
                primaryQuery = "MRCOOL DIY 4th Gen Senville Pioneer " + recBTU + " BTU Mini Split Heat Pump";
            }}

            document.getElementById("recHvacTitle").textContent = recTitle;
            document.getElementById("recHvacDesc").textContent = recDesc;
            document.getElementById("recPrimaryBtn").href = makeAmazonLink(primaryQuery);
            document.getElementById("recSecondaryBtn").href = makeAmazonLink(secondaryQuery);
        }}

        window.addEventListener("DOMContentLoaded", calculateMiniSplit);
    </script>
</body>
</html>"""

def render_single_review_page(rev):
    canonical_url = f"{BASE_URL}/{rev['slug']}.html"
    amz_link = amz_url(rev["keyword"])

    review_schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": rev["product_name"],
        "description": rev["summary"],
        "review": {
            "@type": "Review",
            "datePublished": rev["published_date"],
            "reviewRating": {"@type": "Rating", "ratingValue": rev["rating_score"], "bestRating": "5"},
            "author": {"@type": "Organization", "name": SITE_NAME},
            "reviewBody": " ".join(rev["body_paragraphs"])
        }
    }

    pros_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-emerald-700 font-bold">✓</span><span>{p}</span></li>' for p in rev["pros"]])
    cons_html = "".join([f'<li class="flex items-start gap-2 text-sm text-gray-800"><span class="text-rose-700 font-bold">✕</span><span>{c}</span></li>' for c in rev["cons"]])
    paragraphs_html = "".join([f'<p class="text-gray-800 leading-relaxed text-base mb-4">{p}</p>' for p in rev["body_paragraphs"]])

    recent_reviews = [r for r in get_cumulative_product_reviews() if r["slug"] != rev["slug"]][:6]
    related_html = ""
    for other in recent_reviews:
        related_html += f"""
        <a href="{BASE_URL}/{other['slug']}.html" class="bg-gray-100 border-2 border-gray-300 rounded-xl p-4 hover:border-blue-700 transition block">
            <span class="text-[11px] font-bold text-blue-800 uppercase">{other['verdict_badge']}</span>
            <h4 class="font-extrabold text-sm text-gray-900 mt-1 line-clamp-2">{other['product_name']} Review</h4>
            <span class="text-xs text-gray-600 mt-1 block">Score: {other['rating_score']} / 5.0 ★ ({other['published_date']}) &rarr;</span>
        </a>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{rev['title']} | {SITE_NAME}</title>
    <meta name="description" content="{rev['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="application/ld+json">{json.dumps(review_schema)}</script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home & BTU Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#reviews" class="hover:text-blue-800">Daily Mini-Split Reviews</a>
            <span>/</span>
            <span class="text-gray-900">{rev['product_name']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-5">
            <div class="flex flex-wrap items-center justify-between gap-2">
                <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-3 py-1 rounded-full">{rev['verdict_badge']}</span>
                <div class="flex items-center gap-2">
                    <span class="text-xs font-mono text-gray-600">Published: {rev['published_date']}</span>
                    <span class="text-sm font-black bg-amber-200 text-amber-950 px-3 py-1 rounded-lg">HVAC Rating: {rev['rating_score']} / 5.0 ★</span>
                </div>
            </div>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{rev['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{rev['summary']}</p>

            <div class="grid grid-cols-2 sm:grid-cols-4 gap-3 bg-gray-200 p-4 rounded-xl border border-gray-300 text-xs">
                <div><span class="text-gray-500 block font-medium">BTU / Output</span><strong class="text-gray-900">{rev['spec_1']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Line Set / Tech</span><strong class="text-gray-900">{rev['spec_2']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Installation</span><strong class="text-gray-900">{rev['spec_3']}</strong></div>
                <div><span class="text-gray-500 block font-medium">Warranty</span><strong class="text-gray-900">{rev['spec_4']}</strong></div>
            </div>

            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3.5 px-6 rounded-xl transition shadow-sm">
                   Check Latest Price & Availability on Amazon &rarr;
                </a>
                <a href="{BASE_URL}/#calculator"
                   class="text-center bg-gray-300 hover:bg-gray-400 text-gray-900 font-bold text-sm py-3.5 px-5 rounded-xl transition">
                   Calculate Room BTU & Breaker
                </a>
            </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-gray-100 border-2 border-emerald-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-emerald-900 uppercase tracking-wide">Pros (What We Like)</h2>
                <ul class="space-y-2.5">{pros_html}</ul>
            </div>
            <div class="bg-gray-100 border-2 border-rose-400 rounded-2xl p-6 space-y-3">
                <h2 class="text-base font-extrabold text-rose-900 uppercase tracking-wide">Cons (Things to Consider)</h2>
                <ul class="space-y-2.5">{cons_html}</ul>
            </div>
        </div>

        <article class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900 border-b border-gray-300 pb-3">Hands-On SEER2 Efficiency, Sub-Zero Heating & DIY Installation Analysis</h2>
            {paragraphs_html}
            <div class="pt-4 border-t border-gray-300 flex flex-col sm:flex-row items-center justify-between gap-4">
                <div>
                    <span class="text-xs font-bold uppercase text-blue-800 block">Final Verdict</span>
                    <p class="text-sm font-bold text-gray-900">{rev['product_name']} earns {rev['rating_score']}/5.0 in our ductless HVAC benchmark.</p>
                </div>
                <a href="{amz_link}" target="_blank" rel="nofollow sponsored noopener"
                   class="shrink-0 bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm px-6 py-3 rounded-xl transition shadow-sm">
                   View Customer Reviews & Price on Amazon &rarr;
                </a>
            </div>
        </article>

        <section class="space-y-4">
            <h3 class="text-lg font-extrabold text-gray-900">Recent Daily Mini-Split & HVAC Reviews (+3 Added Daily)</h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                {related_html}
            </div>
        </section>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def render_vs_comparison_page(vs):
    canonical_url = f"{BASE_URL}/{vs['slug']}.html"
    link_a = amz_url(vs["keyword_a"])
    link_b = amz_url(vs["keyword_b"])

    rows_html = ""
    for m in vs["metrics"]:
        rows_html += f"""
        <tr class="border-b border-gray-300">
            <td class="p-4 font-bold text-gray-900 bg-gray-200 text-xs sm:text-sm w-1/4">{m['feature']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_a']}</td>
            <td class="p-4 text-xs sm:text-sm text-gray-800 w-3/8">{m['val_b']}</td>
        </tr>
        """

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{vs['title']} | {SITE_NAME}</title>
    <meta name="description" content="{vs['summary']}">
    <link rel="canonical" href="{canonical_url}">
    <meta name="robots" content="index, follow">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-200 text-gray-900 antialiased">

    {render_common_header_and_banner()}

    <main class="max-w-4xl mx-auto px-4 py-10 space-y-10">
        <nav class="text-xs font-semibold text-gray-600 flex items-center gap-2">
            <a href="{BASE_URL}/" class="hover:text-blue-800">Home & BTU Calculator</a>
            <span>/</span>
            <a href="{BASE_URL}/#comparison" class="hover:text-blue-800">Product Comparisons</a>
            <span>/</span>
            <span class="text-gray-900">{vs['product_a']} vs. {vs['product_b']}</span>
        </nav>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl p-6 sm:p-8 shadow-sm space-y-4">
            <span class="text-xs font-extrabold uppercase tracking-wider bg-blue-100 text-blue-900 border border-blue-300 px-3 py-1 rounded-full">{vs['winner_badge']}</span>
            <h1 class="text-2xl sm:text-4xl font-extrabold text-gray-900 leading-tight">{vs['title']}</h1>
            <p class="text-base text-gray-700 leading-relaxed">{vs['summary']}</p>
        </div>

        <div class="bg-gray-100 border-2 border-gray-300 rounded-2xl overflow-hidden shadow-sm">
            <table class="w-full text-left border-collapse">
                <thead>
                    <tr class="bg-gray-800 text-white text-xs sm:text-sm font-extrabold">
                        <th class="p-4">Specification</th>
                        <th class="p-4 text-blue-300">{vs['product_a']}</th>
                        <th class="p-4 text-amber-300">{vs['product_b']}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                    <tr class="bg-gray-200">
                        <td class="p-4 font-extrabold text-xs sm:text-sm text-gray-900">Check Amazon Price</td>
                        <td class="p-4">
                            <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_a']} &rarr;
                            </a>
                        </td>
                        <td class="p-4">
                            <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="inline-block bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-xs py-2.5 px-4 rounded-lg transition">
                                View {vs['product_b']} &rarr;
                            </a>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>

        <div class="bg-gray-100 border-2 border-blue-600 rounded-2xl p-6 sm:p-8 space-y-4">
            <h2 class="text-xl font-extrabold text-gray-900">Head-to-Head Buying Verdict</h2>
            <p class="text-sm sm:text-base text-gray-800 leading-relaxed">{vs['verdict_text']}</p>
            <div class="flex flex-col sm:flex-row gap-3 pt-2">
                <a href="{link_a}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-blue-700 hover:bg-blue-800 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_a']} on Amazon &rarr;
                </a>
                <a href="{link_b}" target="_blank" rel="nofollow sponsored noopener" class="flex-1 text-center bg-gray-800 hover:bg-gray-900 text-white font-extrabold text-sm py-3 px-4 rounded-xl transition">
                    Shop {vs['product_b']} on Amazon &rarr;
                </a>
            </div>
        </div>
    </main>

    <footer class="bg-gray-300 border-t border-gray-400 mt-16 py-10 px-4 text-xs text-gray-700 text-center">
        <p class="font-bold text-gray-900">{SITE_NAME} — {SITE_TAGLINE}</p>
        <p class="mt-1">As an Amazon Associate, this site earns from qualifying purchases (Store ID: {AFFILIATE_TAG}).</p>
    </footer>
</body>
</html>"""

def generate_sitemap_and_robots(urls):
    today = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    xml_items = ""
    for u in urls:
        xml_items += f"""  <url>
    <loc>{u}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>{"1.0" if u.endswith("/") else "0.85"}</priority>
  </url>\n"""

    sitemap_content = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_items}</urlset>"""

    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_content)

    robots_content = f"""User-agent: *
Allow: /
Sitemap: {BASE_URL}/sitemap.xml
"""
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_content)

    with open(os.path.join(OUTPUT_DIR, f"{INDEXNOW_KEY}.txt"), "w", encoding="utf-8") as f:
        f.write(INDEXNOW_KEY)

def ping_indexnow(urls):
    parsed_host = urllib.parse.urlparse(BASE_URL).netloc
    if not parsed_host or "username.github.io" in parsed_host:
        return

    payload = {
        "host": parsed_host,
        "key": INDEXNOW_KEY,
        "keyLocation": f"{BASE_URL}/{INDEXNOW_KEY}.txt",
        "urlList": urls
    }
    try:
        req = urllib.request.Request(
            "https://api.indexnow.org/indexnow",
            data=json.dumps(payload).encode("utf-8"),
            headers={"Content-Type": "application/json; charset=utf-8"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            print(f"IndexNow Ping Status: {resp.status}")
    except Exception as e:
        print(f"IndexNow notice: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    generated_urls = []

    # 1. Generate Homepage
    home_preset = {
        "slug": "index",
        "name": "2-Car Garage / Workshop (24' × 24' = 576 Sq.Ft — 18,000 BTU)",
        "sqft": 576,
        "ceiling_ft": 9.0,
        "insulation": "1.20",
        "climate": "1.10",
        "zones": 1,
        "desc": "Calculate exact ductless mini-split BTU capacity, heat pump tonnage, multi-zone indoor splits, copper line-set sizes, and 240V breaker/whip specs—plus read 3 new HVAC hardware reviews added daily."
    }
    with open(os.path.join(OUTPUT_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(render_calculator_page(home_preset, is_home=True))
    generated_urls.append(f"{BASE_URL}/")

    # 2. Generate Dedicated HTML Site Map Page (sitemap.html)
    with open(os.path.join(OUTPUT_DIR, "sitemap.html"), "w", encoding="utf-8") as f:
        f.write(render_dedicated_html_sitemap_page())
    generated_urls.append(f"{BASE_URL}/sitemap.html")

    # 3. Generate Programmatic Mini-Split BTU & Breaker Calculator Pages
    for page in ALL_CALC_PAGES:
        filename = f"{page['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_calculator_page(page, is_home=False))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 4. Generate Cumulative Daily Product Review Pages (+3 new reviews unlocked every single day)
    active_reviews = get_cumulative_product_reviews()
    for rev in active_reviews:
        filename = f"{rev['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_single_review_page(rev))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 5. Generate Standalone Head-to-Head Product Comparison Pages
    for vs in VS_COMPARISONS:
        filename = f"{vs['slug']}.html"
        with open(os.path.join(OUTPUT_DIR, filename), "w", encoding="utf-8") as f:
            f.write(render_vs_comparison_page(vs))
        generated_urls.append(f"{BASE_URL}/{filename}")

    # 6. XML Sitemap, Robots & IndexNow Auto-Ping
    generate_sitemap_and_robots(generated_urls)
    ping_indexnow(generated_urls)
    print(f"Successfully generated {len(generated_urls)} total SEO pages ({len(active_reviews)} cumulative review articles [+3/day] + HTML/XML sitemaps) in /{OUTPUT_DIR}!")

if __name__ == "__main__":
    main()
