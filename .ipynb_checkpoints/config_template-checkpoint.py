# import torch
def get_config():
    config = {
        'PALM_API_KEY': 'your_palm_api_key',
        # 'device': torch.device("cuda" if torch.cuda.is_available() else "cpu"),
    }
    
    return config

if __name__ == '__main__':
    print(get_config())