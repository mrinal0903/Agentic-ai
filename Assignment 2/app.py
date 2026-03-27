from agent import create_llm

def generate_report(topic):

    if "AI in Healthcare" in topic:
        return f"""
Cover Page
Title: {topic}

Introduction:
Artificial Intelligence (AI) is transforming healthcare by improving diagnosis, treatment, and patient care. It enables faster decision-making and enhances medical accuracy.

Key Findings:
- AI improves early disease detection through predictive analytics
- Enhances personalized treatment plans using patient data
- Reduces human errors in diagnostics and surgery

Challenges:
- Data privacy and security concerns
- High implementation and maintenance costs

Future Scope:
- AI-powered robotic surgeries
- Integration with wearable health devices

Conclusion:
AI has the potential to revolutionize healthcare by improving efficiency and accuracy, but ethical and cost challenges must be addressed.
"""

    elif "Blockchain" in topic:
        return f"""
Cover Page
Title: {topic}

Introduction:
Blockchain technology improves transparency and traceability in supply chain management. It helps track products from origin to delivery securely.

Key Findings:
- Ensures transparency across the supply chain
- Reduces fraud and counterfeit products
- Enables real-time tracking of goods

Challenges:
- High implementation cost
- Lack of global standardization

Future Scope:
- Integration with IoT for smart tracking
- Use of smart contracts for automation

Conclusion:
Blockchain can significantly improve supply chain systems by increasing trust and efficiency, but adoption barriers still exist.
"""

    else:
        return f"Report generation not available for topic: {topic}"


# ✅ MAIN EXECUTION BLOCK (VERY IMPORTANT)
if __name__ == "__main__":
    print("Starting Project...\n")

    topics = [
        "Impact of AI in Healthcare",
        "Blockchain in Supply Chain"
    ]

    for i, topic in enumerate(topics, start=1):
        print(f"Generating report {i}...\n")

        report = generate_report(topic)

        print(f"\n===== REPORT {i} =====\n")
        print(report)

        with open(f"output{i}.txt", "w", encoding="utf-8") as f:
            f.write(report)

        print(f"Saved as output{i}.txt\n")