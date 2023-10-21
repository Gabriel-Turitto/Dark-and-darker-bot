def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == '!hello':
        return 'Howdy!'
    
    if p_message == '!check_status':
        return 'Gay'
    