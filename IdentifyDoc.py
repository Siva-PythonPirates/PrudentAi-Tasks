def identify_document_type(document_text, forms):
    best_match = None
    max_keywords_matched = 0
    for form_type, keywords in forms.items():
        matched_keywords = sum(1 for keyword in keywords if keyword in document_text)
        if matched_keywords > max_keywords_matched:
            best_match = form_type
            max_keywords_matched = matched_keywords

    return best_match
document_text = input()
forms = {
    "ID Card": ["ID Number", "Date of Birth"],
    "IRS Form": ["Internal Revenue Service", "Taxpayer ID"],
    "Passport": ["Passport Number", "Nationality"],
    "Bank Statement": ["Account Number", "Transaction History"],
}
result = identify_document_type(document_text, forms)
print(result)
