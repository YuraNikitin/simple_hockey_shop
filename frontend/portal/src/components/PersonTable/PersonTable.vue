<template>
    <div class="PersonTable">
      <div class="leader-title">
        Лидеры
        <div class="leader-select">
          <select class="select">
            <option>Лига А</option>
            <option>Лига Б</option>
            <option>Лига С</option>
          </select>
        </div>
      </div>

      <div class="leader-list">
        <div class="leader-item">
          <div class="leader-img">
            <a href="#" class="img-link"> </a>
          </div>

          <div class="leader-info">
            <div class="leader-role">
              Бомбардир
            </div>

            <div class="leader-name">
              <a href="#" class="name-link">Антон Бабышин</a>
            </div>

            <div class="leader-number">
              <a href="#" class="number-link">#55 Вольный</a>
            </div>
          </div>

          <div class="leader-points">
            <div class="leader-points-count">
              12
            </div>

            <div class="leader-points-label">
              Очков
            </div>
          </div>
        </div>

        <div class="leader-item">
          <div class="leader-img">
            <a href="#" class="img-link"> </a>
          </div>

          <div class="leader-info">
            <div class="leader-role">
              Снайпер
            </div>

            <div class="leader-name">
              <a href="#" class="name-link">Максим Юрков</a>
            </div>

            <div class="leader-number">
              <a href="#" class="number-link">#44 Старт</a>
            </div>
          </div>

          <div class="leader-points">
            <div class="leader-points-count">
              7
            </div>

            <div class="leader-points-label">
              Голов
            </div>
          </div>
        </div>

        <div class="leader-item">
          <div class="leader-img">
            <a href="#" class="img-link"> </a>
          </div>

          <div class="leader-info">
            <div class="leader-role">
              Снайпер
            </div>

            <div class="leader-name">
              <a href="#" class="name-link">Антон Бабышин</a>
            </div>

            <div class="leader-number">
              <a href="#" class="number-link">#55 Вольный</a>
            </div>
          </div>

          <div class="leader-points">
            <div class="leader-points-count">
              10
            </div>

            <div class="leader-points-label">
              Пасов
            </div>
          </div>
        </div>

        <div class="leader-item">
          <div class="leader-img">
            <a href="#" class="img-link"> </a>
          </div>

          <div class="leader-info">
            <div class="leader-role">
              Защитник
            </div>

            <div class="leader-name">
              <a href="#" class="name-link">Владислав Малофеев</a>
            </div>

            <div class="leader-number">
              <a href="#" class="number-link">#3 Вольный</a>
            </div>
          </div>

          <div class="leader-points">
            <div class="leader-points-count">
              6
            </div>

            <div class="leader-points-label">
              Очков
            </div>
          </div>
        </div>

        <div class="leader-item">
          <div class="leader-img">
            <a href="#" class="img-link"> </a>
          </div>

          <div class="leader-info">
            <div class="leader-role">
              Вратарь
            </div>

            <div class="leader-name">
              <a href="#" class="name-link">Михаил Казарин</a>
            </div>

            <div class="leader-number">
              <a href="#" class="number-link">#30 Вольный</a>
            </div>
          </div>

          <div class="leader-points">
            <div class="leader-points-count">
              93.6
            </div>

            <div class="leader-points-label">
              %ОБ
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script src="./_PersonTable.js" lang="js"></script>
<style  lang="scss" scoped>
  .PersonTable {


    .leader-title {
      border-bottom: 2px solid #0085d6;
      font-family: Roboto Slab,serif;
      font-size: 19px;
      font-weight: 700;
      line-height: 24px;
      color: #11364e;
      padding-bottom: 10px;
      display: -ms-flexbox;
      display: flex;
      -ms-flex-pack: justify;
      justify-content: space-between;
      -ms-flex-align: center;
      align-items: center;

      .leader-select {
        position: relative;

        .select {
          -webkit-appearance: none;
          -moz-appearance: none;
          appearance: none;
          background-color: #e2eef4;
          border: 1px solid #c5dee9;
          border-radius: 2px;
          height: 45px;
          padding: 0 5px;
          box-sizing: border-box;
          font-size: 13px;
          padding: 0 30px 0 10px;
          font-weight: 400;
        }
      }

      .leader-select::after{
        content: '';
        width: 0;
        height: 0;
        border-left: 7px solid transparent;
        border-top: 7px solid #0085d6;
        border-right: 7px solid transparent;
        display: inline-block;
        position: absolute;
        top: 20px;
        right: 10px;
      }
    }

    .leader-list {
      margin-top: 10px;

      .leader-item {
        height: 95px;
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        border-bottom: 1px solid #c5dee9;
        box-sizing: border-box;

        .leader-img {
          width: 48px;
          height: 48px;
          border-radius: 24px;
          overflow: hidden;
          background: 50% 50% no-repeat;
              background-size: auto;
          background-size: 31px 38px;
          font-size: 0;

          .img-link {
            display: block;
          }
        }

        .leader-info {
          width: 140px;
          margin-left: 5px;

          .leader-role {
            font-family: Roboto Slab,serif;
            font-size: 16px;
            line-height: 16px;
            font-weight: 600;
            color: #0085d6;
          }

          .leader-name {
            .name-link {
              font-size: 13px;
              line-height: 16px;
              color: #11364e;
              text-decoration: none;
              display: block;
              overflow: hidden;
              text-overflow: ellipsis;
              margin-top: 2px;
              white-space: nowrap;
            }
          }

          .leader-number {
            .number-link {
              font-size: 12px;
              color: #0085d6;
              text-decoration: none;
              display: block;
            }
          }
        }

        .leader-points {
          text-align: right;
          width: 41px;

          .leader-points-count {
            font-family: Roboto Slab,serif;
            font-size: 28px;
            line-height: 36px;
            color: #11364e;
          }

          .leader-points-label {
            font-size: 13px;
            line-height: 12px;
            color: #0a2536;
          }
        }
      }
    }
  }
</style>
