<template>
    <div class = "nav">
        <div class = "container my-nav-box">
            <div class ="nav-logo">
              <img src="@/assets/img/logo.svg" alt="#" height = "55px" width = "55px">
              <h2 class = "nav-text-logo">App</h2>
            </div>
            <div class = "nav__menu">
              <div class = "nav__menu-btn>">
                <a href = "accounts/login/">
                  <button type="button" class="nav-btn">Войти</button>
                </a>
              </div>
            </div>
        </div>
    </div>

</template>

<script>
export default{
    name:'nav-bar'
}
</script>

<style lang="scss">
.nav{
    width: 100%;
    background-color: #CE1532;
    height: 75px;
}

.my-nav-box{
    display:flex;
    align-items: center;
    justify-content: space-between;
}

.nav-logo{
    display: flex;
    align-items: center;
}

.nav-logo h2{
    padding-left: 20px;
    color: white;
}

.nav-btn{
    color: #ce1532;
    padding: 5px 10px;
    background-color: #FFBDBD;
    border:none;
    border-radius: 10px;
}

.nav-btn:hover{
    background-color: rgba(255, 189, 189,0.5)
}

</style>