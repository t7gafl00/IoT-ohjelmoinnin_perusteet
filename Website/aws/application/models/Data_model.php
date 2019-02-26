<?php

use Aws\DynamoDb\Exception\DynamoDbException;
use Aws\DynamoDb\Marshaler;

class Data_model extends CI_Model {

    private $sdk, $dynamodb, $marshaler, $tableName, $eav,$params;

    public function __construct()
    {
        parent::__construct();

        require 'aws/aws-autoloader.php';
        date_default_timezone_set('UTC');

        $this->sdk = new Aws\Sdk([
            'region'   => 'eu-west-1',
            'version'  => 'latest',
            'credentials' => [  /* Hard-coding your credentials can be dangerous,
                because it's easy to accidentally commit your credentials into an SCM repository.
                This can potentially expose your credentials to more people than you intend.
                //It can also make it difficult to rotate credentials in the future.
                Do not submit code with hard-coded credentials to your source control. */
                'key'    => '',
                'secret' => '',
            ],
        ]);

        $this->dynamodb = $this->sdk->createDynamoDb();
        $this->marshaler = new Marshaler();
        $this->tableName = 'iot';
        $today_date = date("Y-m-d", time());

        $this->eav = $this->marshaler->marshalJson('
        {
            ":date": "' . $today_date . '"
        }
        ');

        $this->params = [
            'TableName' => $this->tableName,
            'KeyConditionExpression' => '#date = :date',
            'ExpressionAttributeNames'=> [ '#date' => 'date' ],
            'ExpressionAttributeValues'=> $this->eav
        ];
    }

    public function get_data() {
        $result = $this->dynamodb->query($this->params);
        return $result['Items'];
    }
}
