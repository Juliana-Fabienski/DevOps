from src.main import *
from unittest.mock import patch

import pytest

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"mensagem": "Hello World"}


@pytest.mark.asyncio
async def test_funcao():
    with patch('random.randint', return_value=12345):
        result = await funcao()
    assert result == {"teste": True, "num_random": 12345}


@pytest.mark.asyncio
async def test_create_estudante():
    estudante_teste = Estudante(nome='Ciclano', curso='ADS', ativo=False)
    result = await create_estudante(estudante_teste)
    assert estudante_teste == result


@pytest.mark.asyncio
async def test_update_estudante_negative():
    result = await update_estudante(-2)
    assert not result

@pytest.mark.asyncio
async def test_update_estudante_positive():
    result = await update_estudante(7)
    assert result

@pytest.mark.asyncio
async def test_delete_estudante_negative():
    result = await delete_estudante(-1)
    assert not result

@pytest.mark.asyncio
async def test_delete_estudante_positive():
    result = await delete_estudante(2)
    assert result
