<template>
    <div class="TimeTable">
      <div class="match-title">
        События
      </div>

      <div class="match-sub-title">
        Ближайшие матчи
      </div>

      <div class="match-sub-title">
        Прошедшие матчи
      </div>

      <div class="match-day">
        <div class="match-date">
          6 мая 2021/ Четверг
        </div>

        <div class="match-wrapper">
          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                20:15
              </p>
              <p class="match-stadium">
                СЗК "Дизель арена"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  ХК "Вольный"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  ХК "Старт"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                4:2
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>

          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                21:00
              </p>
              <p class="match-stadium">
                "Рубин"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  "ПЛХЛ"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  "Бессоновка"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                3:2
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>

          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                21:15
              </p>
              <p class="match-stadium">
                СЗК "Дизель арена"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  "Эдельвейс"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  ХК "Старт"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                1:6
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>
        </div>
      </div>


      <div class="match-day">
        <div class="match-date">
          28 апреля 2021/ Пятница
        </div>

        <div class="match-wrapper">
          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                20:15
              </p>
              <p class="match-stadium">
                СЗК "Дизель арена"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  ХК "Вольный"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  ХК "Старт"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                4:5
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>

          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                21:00
              </p>
              <p class="match-stadium">
                "Рубин"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  "ПЛХЛ"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  "Бессоновка"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                3:2
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>

          <a class="match-row" href="#">
            <div class="match-place">
              <p class="match-time">
                21:15
              </p>
              <p class="match-stadium">
                СЗК "Дизель арена"
              </p>
            </div>

            <div class="match-teams">
              <div class="match-home">
                <span class="match-home-icon">

                </span>
                <span class="match-home-name">
                  "Эдельвейс"
                </span>
              </div>

              <div class="match-guest">
                <span class="match-name">
                  ХК "Старт"
                </span>
                <span class="match-icon">

                </span>
              </div>
            </div>

            <div class="match-info">
              <p class="match-score">
                4:1
              </p>

              <p class="match-status">
                Окончен
              </p>
            </div>
          </a>
        </div>
      </div>


    </div>
</template>

<script src="./_TimeTable.js" lang="js"></script>
<style lang="scss" scoped>
  .match-title {
    font-family: Roboto Slab,serif;
    font-weight: 700;
    line-height: 24px;
    color: #11364e;
    margin-bottom: 24px;
    border-bottom: 2px solid #0085d6;
  }

  .match-sub-title {
    font-family: Roboto Slab,serif;
    font-weight: 700;
    line-height: 24px;
    color: #11364e;
    margin-bottom: 24px;
  }

  .match-day {
    margin-bottom: 20px;
    color: #11364e;

    .match-date {
      font-family: Roboto Slab,serif;
      font-size: 16px;
      font-weight: 700;
      padding-bottom: 14px;
      border-bottom: 3px solid #c5dee9;
    }

    .match-wrapper {
      position: relative;
      transition: background-color .2s;
      padding-top:10px;

      .match-row {
        display: -ms-flexbox;
        display: flex;
        -ms-flex-align: center;
        align-items: center;
        height: 40px;
        -ms-flex-pack: justify;
        justify-content: space-between;
        border-bottom: 1px solid #c5dee9;
        position: relative;
        text-decoration: none;

        .match-place {
          width: 240px;
          display: -ms-flexbox;
          display: flex;
          -ms-flex-align: center;
          align-items: center;

          .match-time {
            width: 56px;
            height: 24px;
            border-radius: 4px;
            background-color: #e2eef4;
            font-size: 14px;
            color: #11364e;
            display: -ms-flexbox;
            display: flex;
            -ms-flex-pack: center;
            justify-content: center;
            -ms-flex-align: center;
            align-items: center;
            margin: 0 16px 0 0;
          }
          .match-stadium {
            margin: 0;
            font-size: 14px;
            color: #11364e;
          }
        }

        .match-teams {
          width: 300px;
          display: -ms-flexbox;
          display: flex;
          -ms-flex-align: center;
          align-items: center;

          .match-home {
            display: -ms-flexbox;
            display: flex;
            -ms-flex-align: center;
            align-items: center;

            .match-home-icon{
              width: 24px;
              height: 24px;
              display: block;
              text-decoration: none;
              margin: 0 8px;
              position: relative;
              z-index: 1;
            }

            .match-home-name {
              font-size: 14px;
              color: #0085d6;
              position: relative;
              z-index: 1;
            }
          }

          .match-guest {
            display: -ms-flexbox;
            display: flex;
            -ms-flex-align: center;
            align-items: center;

            .match-name {
              font-size: 14px;
              color: #0085d6;
              position: relative;
              z-index: 1;
            }

            .match-icon {
              width: 24px;
              height: 24px;
              display: block;
              text-decoration: none;
              margin: 0 8px;
              position: relative;
              z-index: 1;
            }
          }
          .match-guest::before {
            content: '—';
            display: inline-block;
            margin: 0 3px;
            color: #11364e;
            text-decoration: none;
          }
        }

        .match-info {
          display: -ms-flexbox;
          display: flex;
          -ms-flex-align: center;
          align-items: center;
          width: 125px;

          .match-stage {
            margin: 0;
            font-size: 14px;
            color: #829ba6;
            width: 93px;
          }

          .match-score {
            width: 49px;
            border-radius: 4px;
            background-color: #0085d6;
            font-size: 14px;
            font-weight: 700;
            line-height: 24px;
            color: #fff;
            display: -ms-flexbox;
            display: flex;
            -ms-flex-pack: center;
            justify-content: center;
            -ms-flex-align: center;
            align-items: center;
            margin: 0;
          }

          .match-status {
            margin: 0 8px 0 auto;
            font-size: 14px;
            color: #11364e;
          }
        }
      }
    }
  }
</style>
