/* eslint-disable */
/**
 * devopness API
 * Devopness API - Painless essential DevOps to everyone 
 *
 * The version of the OpenAPI document: latest
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


import { CloudProviderCode } from './cloud-provider-code';
import { ProviderType } from './provider-type';

/**
 * 
 * @export
 * @interface ActionTargetCredentialData
 */
export interface ActionTargetCredentialData {
    /**
     * The unique id of the credential
     * @type {number}
     * @memberof ActionTargetCredentialData
     */
    id: number;
    /**
     * The name of the credential
     * @type {string}
     * @memberof ActionTargetCredentialData
     */
    name: string;
    /**
     * 
     * @type {ProviderType}
     * @memberof ActionTargetCredentialData
     */
    provider_type: ProviderType;
    /**
     * 
     * @type {CloudProviderCode}
     * @memberof ActionTargetCredentialData
     */
    provider_code: CloudProviderCode;
    /**
     * The name of the cloud provider of the credential
     * @type {string}
     * @memberof ActionTargetCredentialData
     */
    provider_name: string;
    /**
     * The human readable version of the provider name
     * @type {string}
     * @memberof ActionTargetCredentialData
     */
    provider_name_human_readable: string;
}

