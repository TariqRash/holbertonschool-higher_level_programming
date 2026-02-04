#!/usr/bin/env python3
"""Simple templating program for generating personalized invitations."""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template.

    Args:
        template: A string containing the template with placeholders.
        attendees: A list of dictionaries containing attendee data.
    """
    # Check input types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return

    if not isinstance(attendees, list):
        print("Error: Attendees is not a list.")
        return

    # Check if all items in attendees are dictionaries
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: Attendees list must contain only dictionaries.")
        return

    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        output = template

        # Replace placeholders with attendee data
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        for placeholder in placeholders:
            value = attendee.get(placeholder)
            # Replace None or missing values with "N/A"
            if value is None:
                value = "N/A"
            output = output.replace("{" + placeholder + "}", str(value))

        # Write to output file
        filename = f"output_{index}.txt"
        with open(filename, 'w') as file:
            file.write(output)
