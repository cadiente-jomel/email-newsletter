$(function () {
    $('.one form .btn').on('click', function (e) {
        let validEmailRegEx = /^[A-Z0-9_'%=+!`#~$*?^{}&|-]+([\.][A-Z0-9_'%=+!`#~$*?^{}&|-]+)*@[A-Z0-9-]+(\.[A-Z0-9-]+)+$/i
        const email = document.querySelector('.email').value;
        let isEmailValid = validEmailRegEx.test(email);
        checkEmail(isEmailValid, email)
        e.preventDefault()
        
       
        return false;
    });

    $('.two .close').on('click', function () {
        $(this).parent().animate(
            {
                top: '-500px',
            },
            500
        );

        $(this).parent().siblings('.one').animate(
            {
                top: '0px',
            },
            500
        );
        return false;
    });

    const checkEmail = (flag, email) => {
      if (flag) {
        let message = 'thank you for subscribing! please check your email'
        displayMessage(message);
        data = {
          email: email
        }
        fetch('/send/welcome/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
          },
          body: JSON.stringify(data)
        })
      }

      else {
        let message = 'You have entered invalid email please try again!'
        displayMessage(message)

    }
    }
    const displayMessage = (textMessage) => {
      let message = document.querySelector('.h3__text')
      message.textContent = textMessage
      $('.one form .btn').parents('.one').animate(
        {
            top: '-500px',
        },
        500
      );

      $('.one form .btn').parents('.one').siblings('.two').animate(
          {
              top: '0px',
          },
          500
      );

    }
});

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

    // const form = document.querySelector('.form')

    // form.addEventListener('submit', e => {

    // })