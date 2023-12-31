from unittest.mock import MagicMock, Mock, patch
import math 


def add(a, b):
    return a + b


class EmailSender:
    def send_email(self, to, subject, body):
        # Interact with real email provider (not shown here for simplicity)
        pass

class Logger:
    def log(self, message):
        # Actual implementation to log messages (not shown for simplicity)
        pass

# main
def perform_complex_calculation(a, b):
    result = add(a, b)
    # Additional complex calculations (for simplicity am just doing a cosine here)
    result = math.cos(result)

    return result

def send_email_and_log(email_sender, logger, to, subject, body):
    email_sender.send_email(to, subject, body)
    logger.log(f"Email sent with subject: {subject}")

@patch("mock_spy_fake_example.add")
def test_complex_calculation_with_mock(add:MagicMock):
    # mock the add class
    add.return_value = 10

    result = perform_complex_calculation(3, 4)

    add.assert_called_once_with(3, 4)
    assert result == -0.8390715290764524 

def test_send_email_and_log_with_spy():
    # Create a spy (MagicMock) for the Logger class
    logger_spy = MagicMock(spec=Logger)

    # Perform the action that uses the logger
    send_email_and_log(MagicMock(), logger_spy, 'user@example.com', 'Test Subject', 'Test Body')

    # Assert that the log method was called with the expected argument
    logger_spy.log.assert_called_once_with('Email sent with subject: Test Subject')


# Using fakes to test the behavior of an email sender


class FakeEmailSender(EmailSender):
    def __init__(self):
        self.sent_emails = []

    def send_email(self, to, subject, body):
        # Simulate sending email by recording it in memory
        self.sent_emails.append({'to': to, 'subject': subject, 'body': body})
        
def test_send_email_and_log_with_fake():
    email_sender_fake = FakeEmailSender()

    send_email_and_log(email_sender_fake, Mock(), 'user@example.com', 'Test Subject', 'Test Body')

    assert len(email_sender_fake.sent_emails) == 1
    assert email_sender_fake.sent_emails[0]['to'] == 'user@example.com'
    assert email_sender_fake.sent_emails[0]['subject'] == 'Test Subject'
    assert email_sender_fake.sent_emails[0]['body'] == 'Test Body'

# # Instantiate the objects
# calculator = Calculator()
# email_sender = EmailSender()
# logger = Logger()

# # Perform a complex calculation
# result = perform_complex_calculation(calculator, 3, 4)
# print(f"Result of complex calculation: {result}")

# # Send an email and log the event
# send_email_and_log(email_sender, logger, 'user@example.com', 'Test Subject', 'Test Body')
