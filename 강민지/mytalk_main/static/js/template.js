const NOTICE_BOX = `
<div class="notice--group {{noti_type}} {{noti_num}}">
    <div class="notice--type">
      <img src={{img_src}} alt="">
    </div>
    <div class="notice--box">
      <div class="notice--box__title"><p>{{title}}</p></div>
      <div class="notice--box__content">{{content}}</div>
      <div class="notice--box__time">{{created_at}}</div>
    </div>
    {{button_type}}
</div>
`;

const NOTICE_BOX_SELECT = `
<div class="notice--btn actions">
    <button class="actions__accept"><img src="../static/icon/Check.svg" alt="수락 버튼">수락</button>
    <button class="actions__reject"><img src="../static/icon/Clear.svg" alt="거절 버튼">거절</button>
</div>
`;

const FRIENDS_LIST = `
<li class="friends--box">
    <input type="checkbox" id="{{name}}" class="group--checkbox" disabled hidden />
    <label class="friends--profile profile {{status}}" data-image="{{profile_picture}}" for="{{name}}"></label>
    <div class="friends--detail">
        <div class="friends__name">{{name}}<span>{{team}}</span></div>
        <div class="friends__status">{{status_message}}</div>          
    </div>
</li>
`;

const CHAT_LIST = `
<li class="room--box {{get_new}}" id="room_num_{{room_num}}" onclick="loadChattingMessageData({{room_num}})">
    <div class="room--profile profile {{user_status}} {{type}}" data-image="{{conv_picture}}"></div>
    <div class="room--detail">
        <input type="hidden">
        <div class="room__name">{{conv_user_name}} <span>{{team}}</span> </div>
        <div class="room__status">{{conv_final_message}}</div>
    </div>
</li>
`;

const MESSAGE_BOX = `
{{message_box__date}}
<div class="message_box {{direction}}">
    <div class="message_box__text" contentEditable="true">{{message}}</div>
    <time class="message_box__time" datetime="{{time}}">{{time}}</time>
</div>
`;