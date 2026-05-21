def process_message(message: str):

    text = message.lower()


    if "sop" in text:
        return (
            "Intent: SOP"
        )

    elif (
        "komplain" in text
        or
        "complaint" in text
    ):

        return (
            "Intent: Complaint"
        )

    elif "menu" in text:

        return (
            "Intent: Menu"
        )


    return (
        "Intent:"
        " General Question"
    )
