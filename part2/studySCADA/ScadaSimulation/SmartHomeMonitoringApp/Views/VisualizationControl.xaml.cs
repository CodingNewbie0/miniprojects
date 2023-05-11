﻿using LiveCharts;
using LiveCharts.Definitions.Charts;
using LiveCharts.Wpf;
using MySql.Data.MySqlClient;
using SmartHomeMonitoringApp.Logics;
using System;
using System.Collections.Generic;
using System.Data;
using System.Diagnostics;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Media;

namespace SmartHomeMonitoringApp.Views
{
    /// <summary>
    /// VisualizationControl.xaml에 대한 상호 작용 논리
    /// </summary>
    public partial class VisualizationControl : UserControl
    {
        List<string> Divisions = null;

        string FirstSensingDate = string.Empty;

        int TotalDataCount = 0;



        public VisualizationControl()
        {
            InitializeComponent();
        }

        private void UserControl_Loaded(object sender, RoutedEventArgs e)
        {
            // 룸선택 콤보박스 초기화
            Divisions = new List<string> { "SELECT", "LIVING", "DINING", "BED", "BATH" };
            CboRoomName.ItemsSource = Divisions;
            CboRoomName.SelectedIndex = 0; // SELECT가 기본 선택

            // 검색시작일 날짜 - DB에서 제일 오래된 날짜와 시간
            using (MySqlConnection conn = new MySqlConnection(Commons.MYSQL_CONNSTRING))
            {
                conn.Open();
                var dtQuery = @"SELECT F.Sensing_Date
                                  FROM (
	                                SELECT DATE_FORMAT(Sensing_DateTime, '%Y-%m-%d') AS Sensing_Date
	                                  FROM smarthomesensor
                                ) AS F
                                 GROUP BY F.Sensing_Date
                                 ORDER BY F.Sensing_Date ASC limit 1";
                MySqlCommand cmd = new MySqlCommand(dtQuery, conn);
                var result = cmd.ExecuteNonQuery();
                Debug.WriteLine(result.ToString());
                FirstSensingDate = DtpStart.Text = result.ToString();
                // 검색종료일은 현재일자로 필터링
                DtpEnd.Text = DateTime.Now.ToString("yyyy-MM-dd");
            }
        }

        // 검색버튼 클릭 이벤트 핸들러
        private async void Button_Click(object sender, RoutedEventArgs e)
        {
            bool isValid = true;
            string errorMsg = string.Empty;
            DataSet ds = new DataSet();

            // 검색, 저장, 수정, 삭제 전 반드시 검증
            if (CboRoomName.SelectedValue.ToString() == "SELECT")
            {
                isValid = false;
                errorMsg += "방 구분을 선택하세요.\n";
            }

            // 시스템 시작된 날짜보다 더 옛날 날짜로 검색
            if (DateTime.Parse(DtpStart.Text) < DateTime.Parse(FirstSensingDate))
            {
                isValid = false;
                errorMsg += $"검색 시작일은 {FirstSensingDate}부터 가능합니다.\n";
            }

            // 오늘날짜 이후 날짜로 검색하려면
            if (DateTime.Parse(DtpEnd.Text) > DateTime.Now)
            {
                isValid = false;
                errorMsg += "검색 종료일은 오늘까지 가능합니다.\n";
            }

            // 검색시작일이 검색종료일보다 이후면
            if (DateTime.Parse(DtpStart.Text)  > DateTime.Parse(DtpEnd.Text))
            {
                isValid = false;
                errorMsg += "검색 시작일이 종료일보다 과거입니다.";
            }

            if (isValid == false)
            {
                await Commons.ShowCustomMessageAsync("검색", errorMsg);
                return;
            }

            // 검색시작
            TotalDataCount = 0;
            try
            {
                using (MySqlConnection conn = new MySqlConnection(Commons.MYSQL_CONNSTRING))
                {
                    conn.Open();
                    var searchQuery = @"SELECT id,
	                                           Home_Id,
	                                           Room_Name,
	                                           Sensing_DateTime,
	                                           Temp,
	                                           Humid
                                          FROM smarthomesensor
                                         WHERE UPPER(Room_Name) = @Room_Name
                                           AND DATE_FORMAT(Sensing_DateTime, '%Y-%m-%d') 
                                       BETWEEN @StartDate AND @EndDate ";
                    MySqlCommand cmd = new MySqlCommand(searchQuery, conn);
                    cmd.Parameters.AddWithValue("@Room_Name", CboRoomName.SelectedValue.ToString());
                    cmd.Parameters.AddWithValue("@StartDate", DtpStart.Text);
                    cmd.Parameters.AddWithValue("@EndDate", DtpEnd.Text);
                    MySqlDataAdapter adapter = new MySqlDataAdapter(cmd);

                    adapter.Fill(ds, "smarthomesensor");

                    // MessageBox.Show(ds.Tables["smarthomesensor"].Rows.Count.ToString(), "TotalData");
                }
            }
            catch (Exception ex)
            {
                await Commons.ShowCustomMessageAsync("DB검색", $"DB검색 오류 {ex.Message}");
            }

            // DB에서 가져온 데이터 차트에 뿌리도록 처리
            if (ds.Tables[0].Rows.Count > 0)
            {

                LineSeries tempSeries = new LineSeries
                {
                    Title = "Temp",
                    Stroke = new SolidColorBrush(Colors.OrangeRed)
                };

                LineSeries humidSeries = new LineSeries
                {
                    Title = "Humid",
                    Stroke = new SolidColorBrush(Colors.Aqua)
                };

                IChartValues tempValues = new ChartValues<double>();
                IChartValues humidValues = new ChartValues<double>();

                foreach (DataRow row in ds.Tables[0].Rows)
                {
                    Convert.ToDouble(row["Temp"]);
                }

                tempSeries.Values = tempValues;
            }
        }
    }
}
