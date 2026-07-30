## Commands


aws --version

    aws configure (En caso de requerir configuracion)
    AWS Access Key ID: _______
    AWS Secret Access Key: _______
    Default region name: _______
    Default output format:



    aws configure list
    cat ~/.aws/credentials
    aws sts get-caller-identity
    echo $AWS_ACCESS_KEY_ID

    aws s3 ls
    aws ec2 describe-instances

    npm install -g aws-cdk  (Agregar paquete)


    cdk init
    cdk init app --language=python


    python3 -m venv .venv
    source .venv/bin/activate

    pip install aws-cdk-lib constructs


    rm -rf cdk.out



    cdk deploy --app "python3 appian_poc_stack.py --profile test-loging"


    cdk deploy --app "python3 appian_poc_stack.py" --profile bold-free-tier


    aws sts get-caller-identity --profile bold-free-tier

    


