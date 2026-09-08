#pragma once
#include <string>
#include "LruCache.hpp"

class Config {
public:
    Config() : cache_(64) {}
    std::string value(const std::string &key) const {
        std::string v;
        if (cache_.get(key, v)) return v;
        return defaults_.count(key) ? defaults_.at(key) : "";
    }
    void set(const std::string &key, const std::string &v) { cache_.put(key, v); }
private:
    LruCache cache_;
    std::map<std::string, std::string> defaults_;
};
