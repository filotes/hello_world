function validateLogin() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
  
    // 进行登录验证的逻辑
    if (username === "root" && password === "114514") {
      alert("登录成功");
      return true; // 允许提交表单
    } else {
      alert("用户名或密码错误");
      return false; // 阻止提交表单
    }
  }