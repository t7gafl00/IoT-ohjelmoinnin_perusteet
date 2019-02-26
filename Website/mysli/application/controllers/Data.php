<?php
class Data extends CI_Controller {

  public function __construct()
  {
    parent::__construct();
    $this->load->model('data_model');
  }

  public function index()
  {
    $this->temperature();
  }

  public function temperature()
  {
    $data['title'] = 'Temperature';
    $data['unit'] = 'Temperature (C)';
    $data['min'] = 0;
    $data['max'] = 30;
    $data['values'] = $this->data_model->get_temperature();
    //print_r($data);
    $data['sensor'] = 'temperature';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph', $data);
    // $this->load->view('templates/footer');
  }

  public function pressure()
  {
    $data['title'] = 'Pressure';
    $data['unit'] = 'Pressure (hPa)';
    $data['min'] = 200;
    $data['max'] = 1100;
    $data['values'] = $this->data_model->get_pressure();
    $data['sensor'] = 'pressure';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph', $data);
  }

  public function humidity()
  {
    $data['title'] = 'Humidity';
    $data['unit'] = 'Humidity (%)';
    $data['min'] = 0;
    $data['max'] = 100;
    $data['values'] = $this->data_model->get_humidity();
    $data['sensor'] = 'humidity';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph', $data);
  }

  public function luminance()
  {
    $data['title'] = 'Luminance';
    $data['unit'] = 'Luminance (lux)';
    $data['min'] = 0;
    $data['max'] = 3000;
    $data['values'] = $this->data_model->get_luminance();
    $data['sensor'] = 'luminance';

    $this->load->view('templates/header');
    $this->load->view('templates/nav');

    $this->load->view('sensors/graph', $data);
  }
}
