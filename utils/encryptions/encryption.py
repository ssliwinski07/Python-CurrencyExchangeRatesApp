from cryptography.fernet import Fernet


class Encryption:

    @staticmethod
    def encrypt_password(password: str, key: str):
        key_bytes = key.encode()
        cipher = Fernet(key_bytes)
        password_to_encrypt = password.encode()
        encrypted_password: str = ""

        try:
            encrypted_password = cipher.encrypt(password_to_encrypt).decode()
        except Exception as e:
            print(f"En error occured during password encryption: {e}")
            return None

        return encrypted_password

    @staticmethod
    def decrypt_password(encrypted_password: str, key: str):
        key_bytes = key.encode()
        cipher = Fernet(key_bytes)

        try:
            decrypted_password = cipher.decrypt(encrypted_password).decode()
        except Exception as e:
            print(f"En error occured during password decryption: {e}")
            return None

        return decrypted_password

    @staticmethod
    def get_encryption_key():
        key = Fernet.generate_key().decode()
        return key
