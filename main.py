from internship_outreach import InternshipOutreach


if __name__ == "__main__":

    # 🔐 Replace with your Gmail + App Password
    SENDER_EMAIL = "agarwalpriyansh384@gmail.com"
    SENDER_PASSWORD = "xpig xypa ugxg kagp"  # Use an App Password for Gmail

    RESUME_PATH = "PRIYAKRITH P S.pdf"

    # ✅ Dummy Contact List
    dummy_contacts = [
        {"email": "ad23b1041@iiitr.ac.in", "name": "John", "company": "AlphaTech"},
        {"email": "priyakrith.ps@gmail.com", "name": "Sarah", "company": "InnovateX"},
        {"email": "anaasin25@gmail.com", "name": "Michael", "company": "NextGen Labs"},
        
    ]

    outreach = InternshipOutreach(
        sender_email=SENDER_EMAIL,
        sender_password=SENDER_PASSWORD,
        resume_path=RESUME_PATH
    )

    outreach.run_campaign(dummy_contacts)