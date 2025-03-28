# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class SpeechToSpeechClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def convert(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: typing.Optional[int] = None,
        audio: core.File,
        model_id: str,
        voice_settings: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Create speech by combining the content and emotion of the uploaded audio with a voice of your choice.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: typing.Optional[int]. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
                                                                0 - default mode (no latency optimizations)
                                                                1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
                                                                2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
                                                                3 - max latency optimizations
                                                                4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

                                                                Defaults to 0.
            - audio: core.File. See core.File for more documentation

            - model_id: str. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

            - voice_settings: str. Voice settings overriding stored setttings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.speech_to_speech.convert(
            voice_id="string",
            optimize_streaming_latency=1,
        )
        """
        with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/speech-to-speech/{jsonable_encoder(voice_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"audio": audio})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    def convert_as_stream(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: typing.Optional[int] = None,
        audio: core.File,
        model_id: str,
        voice_settings: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Create speech by combining the content and emotion of the uploaded audio with a voice of your choice and returns an audio stream.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: typing.Optional[int]. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
                                                                0 - default mode (no latency optimizations)
                                                                1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
                                                                2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
                                                                3 - max latency optimizations
                                                                4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

                                                                Defaults to 0.
            - audio: core.File. See core.File for more documentation

            - model_id: str. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

            - voice_settings: str. Voice settings overriding stored setttings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import ElevenLabs

        client = ElevenLabs(
            api_key="YOUR_API_KEY",
        )
        client.speech_to_speech.convert_as_stream(
            voice_id="string",
            optimize_streaming_latency=1,
        )
        """
        with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/speech-to-speech/{jsonable_encoder(voice_id)}/stream"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"audio": audio})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                for _chunk in _response.iter_bytes():
                    yield _chunk
                return
            _response.read()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncSpeechToSpeechClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def convert(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: typing.Optional[int] = None,
        audio: core.File,
        model_id: str,
        voice_settings: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Create speech by combining the content and emotion of the uploaded audio with a voice of your choice.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: typing.Optional[int]. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
                                                                0 - default mode (no latency optimizations)
                                                                1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
                                                                2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
                                                                3 - max latency optimizations
                                                                4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

                                                                Defaults to 0.
            - audio: core.File. See core.File for more documentation

            - model_id: str. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

            - voice_settings: str. Voice settings overriding stored setttings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.speech_to_speech.convert(
            voice_id="string",
            optimize_streaming_latency=1,
        )
        """
        async with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/speech-to-speech/{jsonable_encoder(voice_id)}"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"audio": audio})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)

    async def convert_as_stream(
        self,
        voice_id: str,
        *,
        optimize_streaming_latency: typing.Optional[int] = None,
        audio: core.File,
        model_id: str,
        voice_settings: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Create speech by combining the content and emotion of the uploaded audio with a voice of your choice and returns an audio stream.

        Parameters:
            - voice_id: str. Voice ID to be used, you can use https://api.elevenlabs.io/v1/voices to list all the available voices.

            - optimize_streaming_latency: typing.Optional[int]. You can turn on latency optimizations at some cost of quality. The best possible final latency varies by model. Possible values:
                                                                0 - default mode (no latency optimizations)
                                                                1 - normal latency optimizations (about 50% of possible latency improvement of option 3)
                                                                2 - strong latency optimizations (about 75% of possible latency improvement of option 3)
                                                                3 - max latency optimizations
                                                                4 - max latency optimizations, but also with text normalizer turned off for even more latency savings (best latency, but can mispronounce eg numbers and dates).

                                                                Defaults to 0.
            - audio: core.File. See core.File for more documentation

            - model_id: str. Identifier of the model that will be used, you can query them using GET /v1/models. The model needs to have support for speech to speech, you can check this using the can_do_voice_conversion property.

            - voice_settings: str. Voice settings overriding stored setttings for the given voice. They are applied only on the given request. Needs to be send as a JSON encoded string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from elevenlabs.client import AsyncElevenLabs

        client = AsyncElevenLabs(
            api_key="YOUR_API_KEY",
        )
        await client.speech_to_speech.convert_as_stream(
            voice_id="string",
            optimize_streaming_latency=1,
        )
        """
        async with self._client_wrapper.httpx_client.stream(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"v1/speech-to-speech/{jsonable_encoder(voice_id)}/stream"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "optimize_streaming_latency": optimize_streaming_latency,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            data=jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings}))
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(remove_none_from_dict({"model_id": model_id, "voice_settings": voice_settings})),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
            files=core.convert_file_dict_to_httpx_tuples(remove_none_from_dict({"audio": audio})),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        ) as _response:
            if 200 <= _response.status_code < 300:
                async for _chunk in _response.aiter_bytes():
                    yield _chunk
                return
            await _response.aread()
            try:
                _response_json = _response.json()
            except JSONDecodeError:
                raise ApiError(status_code=_response.status_code, body=_response.text)
            raise ApiError(status_code=_response.status_code, body=_response_json)
