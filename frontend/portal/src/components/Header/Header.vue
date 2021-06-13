<template>
    <div class="Header" >
      <header :style="{'background-image': 'url(' + require('@/assets/header.jpg') + ')'}">
        <div class="logo">
          <a href="/">
             <img src="@/assets/logo.png"  />
          </a>
        </div>
        <div class="menu">
          <ul>
            <li class="active"><a href="/">О лиге</a></li>
            <li><a href="/">Календарь</a></li>
            <li><a href="/">Новости</a></li>
            <li><a href="/">Медиа</a></li>
            <li><a href="/">Турнирная таблица</a></li>
            <li><a href="/">Игроки</a></li>
            <li><a href="/">Клубы</a></li>
            <li><a href="/">Вход</a></li>
          </ul>
        </div>
      </header>
    </div>
</template>

<script src="./_Header.js" lang="js">

</script>
<style  lang="scss" scoped>
  header {
    display: flex;
    flex-flow: row nowrap;
    justify-content: flex-start;
    align-items: center;
    background-repeat: no-repeat;
    background-size: cover;
    //background: linear-gradient(180deg,#fff 0,#ebf6fd);
    height: 350px;

    .menu {
      flex-grow: 1;
    }

    .menu ul {
      display: flex;
      flex-flow: row nowrap;
      margin: 2px 0 0;
      padding: 0;
      font-size: 15px;
      line-height: 18px;
      list-style: none;
    }

    .menu li {
      margin-right: 20px;
      border-left: 1px solid;
      border-color: white;
    }
    .menu li:last-child {
      margin-right: 0;
    }
    .menu a {
      color: white;
      font-weight: 600;
      text-decoration: none;
    }

    .logo {
      padding:25px;
      margin-right: 60px;
    }

    .menu a,
    .menu .active {
      display: block;
      padding: 8px 10px;
      text-transform: uppercase;
      letter-spacing: .27em;
    }
    .menu .active {
      color: #fff;
      background-color: #c5dee9;
      border-radius: 8px;
    }
  }

</style>
