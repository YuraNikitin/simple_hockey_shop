<template>
    <div class="News">
      <div class="title">
        Медиа
      </div>

      <div class="list">
        <div class="item">
          <div class="img">
            <a class="link">
              <img  src="@/assets/cup.png" alt="ALBUM">
            </a>
          </div>

            <p class="desc">
              <a>Лига "А" Сборная ПЛХЛ - Вольный</a>
            </p>

        </div>
      </div>
    </div>
</template>

<script src="./_News.js" lang="js"></script>
<style lang="scss" scoped>
  .News {
    background-color: #0085d6;
    margin-top: 30px;
    border: 1px solid #c5dee9;
    padding: 30px 25px;
    min-height: 250px;

    .title {
      border-bottom: 2px solid #fff;
      font-family: Roboto Slab,serif;
      font-size: 24px;
      font-weight: 700;
      line-height: 24px;
      color: #fff;
      padding-bottom: 10px;
      display: -ms-flexbox;
      display: flex;
      -ms-flex-pack: justify;
      justify-content: space-between;
      -ms-flex-align: center;
      align-items: center;
    }

    .list {
      display: -ms-flexbox;
      display: flex;
      -ms-flex-pack: justify;
      justify-content: space-between;
      -ms-flex-wrap: wrap;
      flex-wrap: wrap;
      margin-top: 15px;

      .item {
        width: 203px;

        .img {

          .link {
            display: block;
            font-size: 13px;
            line-height: 16px;
            color: #fff;
            text-decoration: none;

            img {
              width: 200px; border: none;
            }
          }
        }

        .desc {
          margin: 15px 0 25px;
          height: 48px;
          overflow: hidden;

          a {
            display: block;
            font-size: 13px;
            line-height: 16px;
            color: #fff;
            text-decoration: none;
          }
        }
      }
    }
}
</style>
