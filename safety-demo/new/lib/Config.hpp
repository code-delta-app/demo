#pragma once
#include <string>
#include "LruCache.hpp"

class Config {
public:
    Config() : cache_(128) {}
    bool has(const std::string &key) const {
        std::string v;
        return cache_.get(key, v) || defaults_.count(key) > 0;
    }
    std::string value(const std::string &key) const {
        std::string v;
        if (cache_.get(key, v)) return v;
        auto it = defaults_.find(key);
        return it == defaults_.end() ? std::string() : it->second;
    }
    void set(const std::string &key, const std::string &v) { cache_.put(key, v); }
private:
    LruCache cache_;
    std::map<std::string, std::string> defaults_;
};
