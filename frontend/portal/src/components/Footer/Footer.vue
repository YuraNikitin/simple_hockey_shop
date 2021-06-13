<template>
    <div class="Footer">
      <footer class="fixed-footer">
        <div class="container">
          <div class="logo">
            ПЕНЗЕНСКАЯ ЛЮБИТЕЛЬСКАЯ ХОККЕЙНАЯ ЛИГА
          </div>

          <div class="menu">
            <ul>
              <li class="active"><a href="/products">О лиге</a></li>
              <li><a href="/">Календарь</a></li>
              <li><a href="/">Новости</a></li>
              <li><a href="/">Медиа</a></li>
              <li><a href="/">Турнирная таблица</a></li>
              <li><a href="/">Регламент</a></li>
            </ul>
          </div>
        </div>


      </footer>
      <div class="copy-right">
        ©ПЛХЛ, 2021г.
      </div>
    </div>
</template>

<script src="./_Footer.js" lang="js"></script>
<style  lang="scss" scoped>
  footer {
    display: flex;
    justify-content: center;
    //background: linear-gradient(180deg,#fff 0,#ebf6fd);
    height: 190px;
    background: #152030;

    .container {
      width: 1200px;
      padding: 0 28px;
      box-sizing: border-box;
      margin: 0 auto;
      position: relative;
      display: flex;


      .logo {
        display: flex;
        color: #fff;
        min-height: 200px;
        align-items: center;
        justify-content: space-between;
      }

      .menu {
        flex-grow: 1;
        display: flex;
        align-items: center;
        justify-content: space-between;
      }

      .menu ul{
        list-style: none;
        display: flex;

      }

      .menu li {
        margin-right: 20px;
      }

      .menu li:last-child {
        margin-right: 0;
      }

      .menu a {
        color: white;
        text-decoration: none;
      }
    }
  }

  .copy-right {
    display: flex;
    justify-content: center;
    background: #152030;
    padding-bottom: 25px;
    color: white;
  }
</style>
