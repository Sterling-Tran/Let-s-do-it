from django.core.mail import send_mail
from celery import shared_task

#asychronouse
@shared_task
def as_send_goal_emails(user_email, friend_email, goal_content):
    # Logic for sending emails
    send_mail(
        'Thử Thách Mới Được Tạo',
        f'Chúc mừng! Bạn đã tạo thử thách mới: {goal_content}. Vui lòng kiểm tra các chi tiết trong hệ thống.',
        'your-email@example.com',
        [user_email],
        fail_silently=False,
    )

    send_mail(
        'Thông Báo Về Thử Thách Mới',
        f'Xin chào! Bạn đã được thông báo về thử thách mới: {goal_content}. Hãy kiểm tra hệ thống để biết thêm chi tiết.',
        'your-email@example.com',
        [friend_email],
        fail_silently=False,
    )
# synchronous
def send_goal_emails(user_email, friend_email, goal_content):
    send_mail(
        'Thử Thách Mới Được Tạo',
        f'Chúc mừng! Bạn đã tạo thử thách mới: {goal_content}. Vui lòng kiểm tra các chi tiết trong hệ thống.',
        'your-email@example.com',
        [user_email],
        fail_silently=False,
    )

    send_mail(
        'Thông Báo Về Thử Thách Mới',
        f'Xin chào! Bạn đã được thông báo về thử thách mới: {goal_content}. Hãy kiểm tra hệ thống để biết thêm chi tiết.',
        'your-email@example.com',
        [friend_email],
        fail_silently=False,
    )
