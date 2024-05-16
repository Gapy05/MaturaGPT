css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://d31nhj1t453igc.cloudfront.net/cloudinary/2022/Apr/08/3EhKAqo8EiH9b6Nz3rKC.jpg" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://theacademic.com/wp-content/uploads/2023/09/neliti_AI_in_teaching_and_learning_4K_ultrarestics_28f38230-ca84-411c-ad90-af1e1000e1b4.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''